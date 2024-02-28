from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ciudad(models.Model):
    nombre=models.CharField(max_length=30, default='N/A')
    class Meta:
        verbose_name="Ciudad"
        verbose_name_plural='Ciudades'

    def __str__(self):
        return '{}'.format(self.nombre)

class Establecimiento(models.Model):
    nombre=models.CharField(max_length=200, default='N/A')
    direccion=models.CharField(max_length=500,default='N/A')
    telefono=models.CharField(max_length=10,default='N/A')
    class Meta:
        verbose_name="Establecimiento"
        verbose_name_plural='Establecimientos'
        
    def __str__(self):
        return '{}'.format(self.nombre)

class Ubicacion(models.Model):
    nombre=models.CharField(max_length=200, default='N/A')
    class Meta:
        verbose_name="Ubicacion"
        verbose_name_plural='Ubicaciones'

    def __str__(self):
        return '{}'.format(self.nombre)

class EstadoActivo(models.Model):
    nombre=models.CharField(max_length=30, default='N/A')
    class Meta:
        verbose_name="Estado"
        verbose_name_plural='Estados'

    def __str__(self):
        return '{}'.format(self.nombre)

class MarcaActivo(models.Model):
    nombre=models.CharField(max_length=30, default='N/A')
    class Meta:
        verbose_name="Marca"
        verbose_name_plural='Marcas'

    def __str__(self):
        return '{}'.format(self.nombre)

class ModeloActivo(models.Model):
    nombre=models.CharField(max_length=30, default='N/A')
    class Meta:
        verbose_name="Modelo"
        verbose_name_plural='Modelos'

    def __str__(self):
        return '{}'.format(self.nombre)

class TipoBienActivo(models.Model):
    nombre=models.CharField(max_length=30, default='N/A')
    class Meta:
        verbose_name="Tipo de Bien"
        verbose_name_plural='Tipos de Bienes'

    def __str__(self):
        return '{}'.format(self.nombre)

class Activo(models.Model):
    codigo=models.CharField(max_length=25, default='N/A')#cambiar el maxleght a 20
    n_serie=models.CharField(max_length=20)
    nombre=models.CharField(max_length=50)
    categoria=models.ForeignKey(TipoBienActivo, on_delete=models.CASCADE,default=None)
    modelo=models.ForeignKey(ModeloActivo, on_delete=models.CASCADE,default=None)
    marca=models.ForeignKey(MarcaActivo, on_delete=models.CASCADE,default=None)
    color=models.CharField(max_length=80, default='N/A')
    estado=models.ForeignKey(EstadoActivo, on_delete=models.CASCADE,default=None)
    ciudad=models.ForeignKey(Ciudad, on_delete=models.CASCADE,default=None)
    establecimiento=models.ForeignKey(Establecimiento, on_delete=models.CASCADE,default=None)
    ubicacion=models.ForeignKey(Ubicacion, on_delete=models.CASCADE,default=None)
    delegado=models.ForeignKey(User, on_delete=models.CASCADE,default=None, null = True, blank = True)
    observaciones=models.TextField()
    mantenimiento=models.BooleanField()
    fecha=models.DateField()
    
    valor=models.DecimalField(max_digits = 5, decimal_places = 2)
    class Meta:
        verbose_name="Activo"
        verbose_name_plural='Activos'

    def __str__(self):
        return '{}'.format(self.nombre)

# agregar valor y serie, quitar delegado, crear una tabla de asignacion, el asignado puede ser asignado con varios  bienes
# crear una tabla de custodio y al custodio asignarle bienes
