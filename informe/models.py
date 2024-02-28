from django.db import models
from django.contrib.auth.models import User
from activos.models import Activo

# Create your models here.
class Informe(models.Model):
    nombre_tipobienactivo=models.CharField(max_length=30, default='N/A')
    activo=models.ForeignKey(Activo,on_delete=models.CASCADE)
    revisor=models.ForeignKey(User,on_delete=models.CASCADE,related_name='revisor_informe')
    director=models.ForeignKey(User,on_delete=models.CASCADE,related_name='director_informe')
    codigo_acta=models.CharField(max_length=10, default='N/A')
    informe=models.TextField()
    fecha=models.DateField()
    
    class Meta:
        verbose_name="Informe"
        verbose_name_plural='Informes'

    def __str__(self):
        return self.informe