from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect 
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User, Group
from django.db import transaction
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


# Create your views here.
def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    user.save()

def login_auth(request):
    print(request)
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('activos:activos_index')
        else:
            messages.success(request,'Usuario y contraseña incorrectos')
            return redirect(reverse('login'))
        
                
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

@transaction.atomic
def usuario_create(request):
    my_group = Group.objects.get(name='Delegado')
    form = SignUpForm()
    form2 = UsuarioForm()
    print(form, form2)
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        form2 = UsuarioForm(request.POST)
        print("creando usuario")
        if form.is_valid() and form2.is_valid():
            user = form.save()
            usuario = Usuario.objects.get(user = user)
            usuario.ci_ruc = form2.cleaned_data.get('ci_ruc')
            usuario.cargo = form2.cleaned_data.get('cargo')
            usuario.direccion = form2.cleaned_data.get('direccion')
            usuario.telefono = form2.cleaned_data.get('telefono')
            usuario.ciudad = form2.cleaned_data.get('ciudad')
            usuario.save()
            my_group.user_set.add(user)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            print(form2.cleaned_data)
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return redirect('usuarios:usuario_list')
        else:
            context = {
                'form':form,
                'form2':form2
            }
            # messages.error(request, form.errors)
            # messages.error(request, form2.errors)
            return render(request, 'usuarios/usuario_create.html', context)
    context = {
        'form':form,
        'form2':form2
    }
    return render(request, 'usuarios/usuario_create.html', context)



def usuario_pdf(request):
    usuarios = Usuario.objects.all().order_by('id')
    usuario_ci = Usuario.objects.all()
    context = {
        'usuarios':usuarios,
        'usuario_ci':usuario_ci,
        'title': "Listado Usuarios",
        'cantidad':usuarios.count()
    }
    return render(request, 'usuarios/usuario_pdf.html', context)


def usuario_list(request):
    usuarios = Usuario.objects.all().order_by('id')
    usuario_ci = Usuario.objects.all()
    context = {
        'usuarios':usuarios,
        'usuario_ci':usuario_ci,
        'title': "Listado Usuarios"
    }
    return render(request, 'usuarios/usuario_list.html', context)

def usuario_edit(request, id_user):
    user = User.objects.get(id = id_user)
    usuario = Usuario.objects.get(user = user)
    form = UsuarioForm(instance = usuario)
    form2 = SignUpForm(instance = user)

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        form2 = SignUpForm(request.POST, instance=user)

        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
        return redirect('usuarios:usuario_list')
    return render(request, 'usuarios/usuario_edit.html',{'form':form, 'form2':form2})

def usuario_delete(request, id_user):
    user = User.objects.get(id = id_user)
    if request.method == 'POST':
        user.delete()
        return redirect('usuarios:usuario_list')
    return render(request, 'usuarios/usuario_delete.html',{'user':user})

class usuario_detail(DetailView):
    model = Usuario
    template_name = 'usuarios/usuario_detail.html'
    success_url = reverse_lazy('usuarios:usuario_list')
    

