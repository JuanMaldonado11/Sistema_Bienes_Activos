from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from django.contrib.auth.decorators import login_required
from activos import views
from django.shortcuts import render,get_object_or_404


router=routers.DefaultRouter()
router.register(r'ciudad',views.CiudadViewSet)
router.register(r'establecimiento',views.EstablecimientoViewSet)
router.register(r'ubicacion',views.UbicacionViewSet)
router.register(r'estadoactivo',views.EstadoActivoViewSet)
router.register(r'marcactivo',views.MarcaActivoViewSet)
router.register(r'modeloactivo',views.ModeloActivoViewSet)
router.register(r'tipobienactivo',views.TipoBienActivoViewSet)
router.register(r'activo',views.ActivoViewSet)
urlpatterns =[
    path ('activos_index', login_required(views.index), name='activos_index'),
    #url(r'index', index, name='index'),
    #url('activos_form', views.activos_view, name='activos_form'),
    #url(r'activos_list', views.activos_list, name='activos_list'),
    #url(r'^activos_edit/(?P<id_activos>[0-9]+)/$', views.activo_edit, name='activos_edit'),
    path('activos_list', login_required(views.activos_list), name='activos_list'),
    path('activo_pdf', login_required(views.activos_pdf), name='activo_pdf'),
    # path('asignacion_pdf', login_required(views.ListActivosPdf.as_view()), name='activo_pdf'),
    path('activo_registroPdf/<pk>/', login_required(views.pdfregistro.as_view()), name='activo_registroPdf'),
    path('asignacion_pdf/<int:id_usuarios>/', login_required(views.asignacion_pdf), name='asignacion_pdf'),
    path('generar_qr/<int:activo_pk>/<str:tipo_qr>/', views.generar_qr, name='generar_qr'),
    
    #segundo codigo qr 
    path('qr_adhesivo/<int:delegado_pk>/', login_required ( views.qr_adhesivo), name='qr_adhesivo'),
    path('detalle_qr_adesivo/<int:delegado_pk>/', login_required ( views.detalle_qr_adesivo), name='detalle_qr_adesivo'),
    path('activos/segundo_qr/<int:adhesivo_pk>/', views.segundo_qr, name='segundo_qr'),




    path('asignacion_list', login_required(views.asignacion_list), name='asignacion_list'),
    path('asignacion_groups', login_required(views.asignacion_groups), name='asignacion_groups'),

    path('activos_form/', login_required(views.activos_view), name='activos_form'),
    path('activos_edit/<int:id_activos>/', login_required(views.activos_edit), name = 'activos_edit'),
    path('asignacion_delegado/<int:id_activos>/', login_required(views.asignacion_delegado), name = 'asignacion_delegado'),
    path('activos_delete/<int:id_activos>/', login_required(views.activos_delete), name='activos_delete'),
    path('activos_detail/<pk>/', login_required(views.activos_detail.as_view()), name='activos_detail'),
    path(r'^', include(router.urls)),
    path(r'^api-auth',include('rest_framework.urls',namespace='rest_framework')),
    path('ciudad_list', login_required(views.CiudadList.as_view()), name='ciudad_list'),
    path('ciudad_create', login_required(views.CiudadCreate.as_view()), name='ciudad_create'),
    path('ciudad_edit/<pk>/', login_required(views.Ciudad_edit.as_view()), name = 'ciudad_edit'),
    path('ciudad_delete/<pk>/', login_required(views.Ciudad_delete.as_view()), name='ciudad_delete'),
    path('establecimiento_list', login_required(views.EstablecimientoList.as_view()), name='establecimiento_list'),
    path('establecimiento_create', login_required(views.EstablecimientoCreate.as_view()), name='establecimiento_create'),
    path('establecimiento_edit/<pk>/', login_required(views.Establecimiento_edit.as_view()), name = 'establecimiento_edit'),
    path('establecimiento_delete/<pk>/', login_required(views.Establecimiento_delete.as_view()), name='establecimiento_delete'),
    path('ubicacion_list', login_required(views.UbicacionList.as_view()), name='ubicacion_list'),
    path('ubicacion_create', login_required(views.UbicacionCreate.as_view()), name='ubicacion_create'),
    path('ubicacion_edit/<pk>/', login_required(views.Ubicacion_edit.as_view()), name = 'ubicacion_edit'),
    path('ubicacion_delete/<pk>/', login_required(views.Ubicacion_delete.as_view()), name='ubicacion_delete'),
    path('estado_list', login_required(views.EstadoActivoList.as_view()), name='estado_list'),
    path('estado_create', login_required(views.EstadoActivoCreate.as_view()), name='estado_create'),
    path('estado_edit/<pk>/', login_required(views.Estado_edit.as_view()), name = 'estado_edit'),
    path('estado_delete/<pk>/', login_required(views.Estado_delete.as_view()), name='estado_delete'),
    path('marca_list', login_required(views.MarcaActivoList.as_view()), name='marca_list'),
    path('marca_create', login_required(views.MarcaActivoCreate.as_view()), name='marca_create'),
    path('marca_edit/<pk>/', login_required(views.Marca_edit.as_view()), name = 'marca_edit'),
    path('marca_delete/<pk>/', login_required(views.Marca_delete.as_view()), name='marca_delete'),
    path('modelo_list', login_required(views.ModeloActivoList.as_view()), name='modelo_list'),
    path('modelo_create', login_required(views.ModeloActivoCreate.as_view()), name='modelo_create'),
    path('modelo_edit/<pk>/', login_required(views.Modelo_edit.as_view()), name = 'modelo_edit'),
    path('modelo_delete/<pk>/', login_required(views.Modelo_delete.as_view()), name='modelo_delete'),
    path('tipobien_list', login_required(views.TipoBienList.as_view()), name='tipobien_list'),
    path('tipobien_create', login_required(views.TipoBienCreate.as_view()), name='tipobien_create'),
    path('tipobien_edit/<pk>/', login_required(views.TipoBien_edit.as_view()), name = 'tipobien_edit'),
    path('tipobien_delete/<pk>/', login_required(views.TipoBien_delete.as_view()), name='tipobien_delete'),
    
]