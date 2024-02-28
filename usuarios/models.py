from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from activos.models import Activo
from django.contrib.auth.signals import user_logged_in

# Create your models here.

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  null=False, blank=False, editable=False)
    ci_ruc = models.CharField(max_length=13, help_text='Cedula o RUC')
    cargo = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=50, default='Loja')
    login_count = models.PositiveIntegerField(default=0)
    
    class Meta: 
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
    
    def __str__(self):
        return self.user.username

def login_user(sender, request, user, **kwargs):
    user.usuario.login_count = user.usuario.login_count + 1
    user.usuario.save()

user_logged_in.connect(login_user)

    
        
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.usuario.save()
