"""sistema_activos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.static import static
from django.conf import settings
# from django.conf.urls import url
from usuarios import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns=[
    path('admin/', admin.site.urls),
    path('qr_code/', include('qr_code.urls', namespace="qr_code")),
    path(r'activos/', include(('activos.urls','activos'),namespace='activos')),
    path('app/', include('app.urls')),
    path(r'informe/', include(('informe.urls','informe'),namespace='informe')),
    path(r'usuarios/', include(('usuarios.urls','usuarios'),namespace='usuarios')),
    path(r'^login/$', views.login_auth, name = 'login'),
    path(r'^logout/', LogoutView.as_view(template_name= 'logout.html'), name = 'logout'),
    path(r'^resets/password_reset_form/', PasswordResetView.as_view(),{'template_name':'registrations/password_reset_form.html',
    'email_template_name':'registrations/password_reset_email.html'}, name='password_reset_form'),
    path(r'^resets/password_reset_done/', PasswordResetDoneView.as_view(),{'template_name':'registrations/password_reset_done.html'},
     name='password_reset_done'),
    path(r'^resets/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(),{'template_name':'registrations/password_reset_confirm.html'},
     name='password_reset_confirm'),
    path(r'^resets/password_reset_complete/', PasswordResetCompleteView.as_view(),{'template_name':'registrations/password_reset_complete.html'},
     name='password_reset_complete'),
]
