from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    '''Admin View for Usuario'''

    list_display = (
        'user',
        'ci_ruc',
        'cargo',
        'direccion',
        'telefono',
        'ciudad',
        'login_count',
        )
    list_filter = ('cargo',)
    
   