from django.contrib import admin
from .models import *
admin.site.register(Ciudad)
admin.site.register(Establecimiento)
admin.site.register(Ubicacion)
admin.site.register(EstadoActivo)
admin.site.register(MarcaActivo)
admin.site.register(ModeloActivo)
admin.site.register(TipoBienActivo)
@admin.register(Activo)
class ActivoAdmin(admin.ModelAdmin):
    '''Admin View for Activo'''

    list_display = (
        'id',
        'codigo',
        'nombre',
        'categoria',
        'mantenimiento',
        )
    
