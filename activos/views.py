from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from activos.models import Ciudad,Establecimiento,Ubicacion,EstadoActivo,MarcaActivo,ModeloActivo,TipoBienActivo,Activo
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from activos.serializers import CiudadSerializer,EstablecimientoSerializer,UbicacionSerializer,EstadoActivoSerializer,MarcaActivoSerializer,ModeloActivoSerializer,EstadoActivoSerializer,TipoBienActivoSerializer,ActivoSerializer
from django.db.models import Max
from activos.forms import *
from usuarios.models import *
from django.urls import reverse





@method_decorator(login_required, name='dispatch')
class CiudadViewSet(viewsets.ModelViewSet):
    queryset=Ciudad.objects.all().order_by('nombre')
    serializer_class=CiudadSerializer

@method_decorator(login_required, name='dispatch')
class EstablecimientoViewSet(viewsets.ModelViewSet):
    queryset=Establecimiento.objects.all().order_by('nombre')
    serializer_class=EstablecimientoSerializer

@method_decorator(login_required, name='dispatch')
class UbicacionViewSet(viewsets.ModelViewSet):
    queryset=Ubicacion.objects.all().order_by('nombre')
    serializer_class=UbicacionSerializer

@method_decorator(login_required, name='dispatch')
class EstadoActivoViewSet(viewsets.ModelViewSet):
    queryset=EstadoActivo.objects.all().order_by('nombre')
    serializer_class=EstadoActivoSerializer

@method_decorator(login_required, name='dispatch')
class MarcaActivoViewSet(viewsets.ModelViewSet):
    queryset=MarcaActivo.objects.all().order_by('nombre')
    serializer_class=MarcaActivoSerializer

@method_decorator(login_required, name='dispatch')
class ModeloActivoViewSet(viewsets.ModelViewSet):
    queryset=ModeloActivo.objects.all().order_by('nombre')
    serializer_class=ModeloActivoSerializer

@method_decorator(login_required, name='dispatch')
class TipoBienActivoViewSet(viewsets.ModelViewSet):
    queryset=TipoBienActivo.objects.all().order_by('nombre')
    serializer_class=TipoBienActivoSerializer

@method_decorator(login_required, name='dispatch')
class ActivoViewSet(viewsets.ModelViewSet):
    queryset=Activo.objects.all().order_by('nombre')
    serializer_class=ActivoSerializer

# Crea tus vistas aqui.
@login_required
def index (request):
    import json
    import datetime
    today = datetime.date.today()
    last_monday = today - datetime.timedelta(days=today.weekday())
    next_monday = today + datetime.timedelta(days=-today.weekday(), weeks=1)

    bienes_semanales = Activo.objects.filter(fecha__range = [last_monday, next_monday])
    usuarios = Usuario.objects.all().order_by('-login_count')[:3]
    usuarios = list(usuarios.values_list('user__username', 'login_count'))
    usuarios_dict = []
    array_buen_estado = []
    array_mal_estado = []
    # Consulta de usuaios por login
    for usuario in usuarios:
        usuarios_dict.append([usuario[0], usuario[1]]) 

  
    for i  in range(1, 8):
        array_buen_estado.append(bienes_semanales.filter(fecha__week_day = i, estado__nombre = 'Bueno').count()) 
        array_mal_estado.append(bienes_semanales.filter(fecha__week_day = i, estado__nombre = 'Malo').count()) 

    print(array_buen_estado)
    print(array_mal_estado)
    context = {
        'usuarios': usuarios,
        'usuarios_dict': json.dumps(usuarios_dict),
        'array_buen_estado': json.dumps(array_buen_estado),
        'array_mal_estado': json.dumps(array_mal_estado),
    }
    return render(request, 'app/index.html', context)



@login_required
def activos_view(request):
    if request.method == 'POST':
        form = ActivosForm(request.POST)
        print("creando activo")
        if form.is_valid():
            form.save()
        return redirect('activos:activos_list')
    else:
        form = ActivosForm()
    return render(request, 'activos/activos_form.html',{'form':form})

@login_required
def activos_list(request):
    activos = Activo.objects.all()
    contexto = {
        'activos':activos,
        'title': "Listado Activos",
    }
    return render(request, 'activos/activos_list.html', contexto) 

@login_required
def activos_pdf(request):
    activos = Activo.objects.all()
    contexto = {
        'activos':activos,
        'cantidad':activos.count(),
        'title': "Listado Activos",
    }
    return render(request, 'activos/activo_pdf.html', contexto) 



@login_required
def asignacion_groups(request):
    activos = Activo.objects.all()
    delegados = User.objects.filter(groups__name = 'Delegado')
    activos_list = []
    for delegado in delegados:
        activos_delegado = Activo.objects.filter(delegado = delegado)
        activo_object = {
            'delegado': delegado,
            'activos': activos_delegado,
        }
        activos_list.append(activo_object) 
    print(activos_list)
    return render(request, 'activos/asignacion_groups.html', {'activos_list':activos_list}) 

@login_required
def asignacion_pdf(request, id_usuarios):
    delegados = User.objects.get(id = id_usuarios)
    activos = Activo.objects.filter(delegado = delegados)
    cedula = Usuario.objects.get(user = delegados)
    print(cedula.ci_ruc)
    
    usuarios = Usuario.objects.all()
    contexto = {
        'activos' : activos,
        'delegados' : delegados, 
        'usuarios' : usuarios,
        'cedula' : cedula
    }
    print(contexto)
    return render(request, 'activos/asignacion_pdf.html', contexto) 

 
class pdfregistro(DetailView):
    model = Activo
    template_name =  'activos/activo_registroPdf.html'
#primero qr

def generar_qr(request, activo_pk, tipo_qr):
    print(tipo_qr)
    import qrcode
    from io import BytesIO
    from urllib.parse import urlparse
    inicio_url = request.scheme + '://' + request.get_host()
    url = ''
    if tipo_qr == '0':
        url = f"{inicio_url}/activos/activos_edit/{activo_pk}/"
    else:
        # activo_pk llega a ser delegado_pk
        url = f"{inicio_url}/activos/detalle_qr_adesivo/{activo_pk}/"

    qr = qrcode.make(url) 
    buffer = BytesIO()
    qr.save(buffer)
    image_bytes = buffer.getvalue()
    return HttpResponse(image_bytes, content_type="image/png")

def detalle_qr_adesivo(request, delegado_pk):
    delegado = User.objects.get(id = delegado_pk)
    activos = Activo.objects.filter(delegado = delegado)
    context = {
        'activos':activos
    }

    return render(request, 'activos/detalle_qr_adesivo.html', context)



#segundo codigo qr
def segundo_qr(request, adhesivo_pk):
    import qrcode
    from io import BytesIO
    from urllib.parse import urlparse
    # Construye la URL deseada utilizando la vista 'activos_detail2' y los parámetros 'nombre' y 'numero_serie'
    inicio_url = request.scheme + '://' + request.get_host()
    url = f"{inicio_url}/asignación_pdf/{adhesivo_pk}/"
    # Esta vista genera el código QR basado en el nombre y el número de serie
    qr =qrcode.make(url)
    buffer = BytesIO()
    qr.save(buffer)
    image_bytes = buffer.getvalue()
    return HttpResponse(image_bytes, content_type="image/png")

@login_required
def asignacion_list(request):
    activos = Activo.objects.all()
    contexto = {
        'activos':activos,
        'title': "Listado Asignacion",
    }
    return render(request, 'activos/asignacion_list.html', contexto)

@login_required
def asignacion_delegado(request, id_activos):
    activos = Activo.objects.get(id = id_activos)
    if request.method == 'GET':
        form = DelegadoForm(instance=activos)
    else:
        form = DelegadoForm(request.POST, instance=activos)
        if form.is_valid():
            form.save()
        return redirect('activos:asignacion_list')
    return render(request, 'activos/asignacion_delegado.html',{'form':form})

@login_required
def activos_edit(request, id_activos):
    activos = Activo.objects.get(id = id_activos)
    if request.method == 'GET':
        form = ActivosForm(instance=activos)
    else:
        form = ActivosForm(request.POST, instance=activos)
        if form.is_valid():
            form.save()
        return redirect('activos:activos_list')
    return render(request, 'activos/activos_form.html',{'form':form})

@login_required
def activos_delete(request, id_activos):
    activos = Activo.objects.get(id=id_activos)
    if request.method == 'POST':
        activos.delete()
        return redirect('activos:activos_list')
    return render(request, 'activos/activos_delete.html',{'activos':activos})

#segundo codigo qr
def qr_adhesivo(request, delegado_pk):
    activos =  Activo.objects.filter(delegado__pk = delegado_pk)
    print(activos)
    context = { 
        'activos':activos
    }
    # Aquí va la lógica de tu vista para generar el QR adhesivo
    # Puedes renderizar un template o devolver una respuesta HTTP con el QR
    return render(request, 'activos/qr_adhesivo.html', context)


@method_decorator(login_required, name='dispatch')
class activos_detail(DetailView):
    model = Activo
    template_name = 'activos/activos_detail.html'

@method_decorator(login_required, name='dispatch')
class CiudadList(ListView):
    model = Ciudad
    template_name = 'activos/ciudad_list.html'

@method_decorator(login_required, name='dispatch')
class CiudadCreate(CreateView):
    model = Ciudad
    form_class = CiudadForm
    template_name = 'activos/ciudad_create.html'
    success_url = reverse_lazy('activos:ciudad_list')

@method_decorator(login_required, name='dispatch')
class Ciudad_edit(UpdateView):
    model = Ciudad
    form_class = CiudadForm
    template_name = 'activos/ciudad_create.html'
    success_url = reverse_lazy('activos:ciudad_list')

@method_decorator(login_required, name='dispatch')
class Ciudad_delete(DeleteView):
    model = Ciudad
    form_class = CiudadForm
    template_name = 'activos/ciudad_delete.html'
    success_url = reverse_lazy('activos:ciudad_list')

@method_decorator(login_required, name='dispatch')
class EstablecimientoList(ListView):
    model = Establecimiento
    template_name = 'activos/establecimiento_list.html'

@method_decorator(login_required, name='dispatch')
class EstablecimientoCreate(CreateView):
    model = Establecimiento
    form_class = EstablecimientoForm
    template_name = 'activos/establecimiento_create.html'
    success_url = reverse_lazy('activos:establecimiento_list')

@method_decorator(login_required, name='dispatch')
class Establecimiento_edit(UpdateView):
    model = Establecimiento
    form_class = EstablecimientoForm
    template_name = 'activos/establecimiento_create.html'
    success_url = reverse_lazy('activos:establecimiento_list')

@method_decorator(login_required, name='dispatch')
class Establecimiento_delete(DeleteView):
    model = Establecimiento
    form_class = EstablecimientoForm
    template_name = 'activos/establecimiento_delete.html'
    success_url = reverse_lazy('activos:establecimiento_list')

@method_decorator(login_required, name='dispatch')
class UbicacionList(ListView):
    model = Ubicacion
    template_name = 'activos/ubicacion_list.html'

@method_decorator(login_required, name='dispatch')
class UbicacionCreate(CreateView):
    model = Ubicacion
    form_class = UbicacionForm
    template_name = 'activos/ubicacion_create.html'
    success_url = reverse_lazy('activos:ubicacion_list')

@method_decorator(login_required, name='dispatch')
class Ubicacion_edit(UpdateView):
    model = Ubicacion
    form_class = UbicacionForm
    template_name = 'activos/ubicacion_create.html'
    success_url = reverse_lazy('activos:ubicacion_list')

@method_decorator(login_required, name='dispatch')
class Ubicacion_delete(DeleteView):
    model = Ubicacion
    form_class = UbicacionForm
    template_name = 'activos/ubicacion_delete.html'
    success_url = reverse_lazy('activos:ubicacion_list')

@method_decorator(login_required, name='dispatch')
class EstadoActivoList(ListView):
    model = EstadoActivo
    template_name = 'activos/estado_list.html'

@method_decorator(login_required, name='dispatch')
class EstadoActivoCreate(CreateView):
    model = EstadoActivo
    form_class = EstadoActivoForm
    template_name = 'activos/estado_create.html'
    success_url = reverse_lazy('activos:estado_list')

@method_decorator(login_required, name='dispatch')
class Estado_edit(UpdateView):
    model = EstadoActivo
    form_class = EstadoActivoForm
    template_name = 'activos/estado_create.html'
    success_url = reverse_lazy('activos:estado_list')

@method_decorator(login_required, name='dispatch')
class Estado_delete(DeleteView):
    model = EstadoActivo
    form_class = EstadoActivoForm
    template_name = 'activos/estado_delete.html'
    success_url = reverse_lazy('activos:estado_list')

@method_decorator(login_required, name='dispatch')
class MarcaActivoList(ListView):
    model = MarcaActivo
    template_name = 'activos/marca_list.html'

@method_decorator(login_required, name='dispatch')
class MarcaActivoCreate(CreateView):
    model = MarcaActivo
    form_class = MarcaActivoForm
    template_name = 'activos/marca_create.html'
    success_url = reverse_lazy('activos:marca_list')

@method_decorator(login_required, name='dispatch')
class Marca_edit(UpdateView):
    model = MarcaActivo
    form_class = MarcaActivoForm
    template_name = 'activos/marca_create.html'
    success_url = reverse_lazy('activos:marca_list')

@method_decorator(login_required, name='dispatch')
class Marca_delete(DeleteView):
    model = MarcaActivo
    form_class = ModeloActivoForm
    template_name = 'activos/marca_delete.html'
    success_url = reverse_lazy('activos:marca_list')

@method_decorator(login_required, name='dispatch')
class ModeloActivoList(ListView):
    model = ModeloActivo
    template_name = 'activos/modelo_list.html'

@method_decorator(login_required, name='dispatch')
class ModeloActivoCreate(CreateView):
    model = ModeloActivo
    form_class = ModeloActivoForm
    template_name = 'activos/modelo_create.html'
    success_url = reverse_lazy('activos:modelo_list')

@method_decorator(login_required, name='dispatch')
class Modelo_edit(UpdateView):
    model = ModeloActivo
    form_class = ModeloActivoForm
    template_name = 'activos/modelo_create.html'
    success_url = reverse_lazy('activos:modelo_list')

@method_decorator(login_required, name='dispatch')
class Modelo_delete(DeleteView):
    model = ModeloActivo
    form_class = ModeloActivoForm
    template_name = 'activos/modelo_delete.html'
    success_url = reverse_lazy('activos:modelo_list')

@method_decorator(login_required, name='dispatch')
class TipoBienList(ListView):
    model = TipoBienActivo
    template_name = 'activos/tipobien_list.html'

@method_decorator(login_required, name='dispatch')
class TipoBienCreate(CreateView):
    model = TipoBienActivo
    form_class = TipoBienForm
    template_name = 'activos/tipobien_create.html'
    success_url = reverse_lazy('activos:tipobien_list')

@method_decorator(login_required, name='dispatch')
class TipoBien_edit(UpdateView):
    model = TipoBienActivo
    form_class = TipoBienForm
    template_name = 'activos/tipobien_create.html'
    success_url = reverse_lazy('activos:tipobien_list')

@method_decorator(login_required, name='dispatch')
class TipoBien_delete(DeleteView):
    model = TipoBienActivo
    form_class = TipoBienForm
    template_name = 'activos/tipobien_delete.html'
    success_url = reverse_lazy('activos:tipobien_list')