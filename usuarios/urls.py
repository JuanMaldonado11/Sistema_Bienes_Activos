from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.conf.urls import include
from usuarios import views

urlpatterns=[
    path('usuario_list', login_required(views.usuario_list), name='usuario_list'),
    path('usuario_create', login_required(views.usuario_create), name='usuario_create'),
    path('usuario_edit/<int:id_user>/', login_required(views.usuario_edit), name='usuario_edit'),
    path('usuario_delete/<int:id_user>/', login_required(views.usuario_delete), name='usuario_delete'),
    path('usuarios_detail/<pk>/', login_required(views.usuario_detail.as_view()), name='usuario_detail'),
    path('usuario_pdf', login_required(views.usuario_pdf), name='usuario_pdf'),



]
