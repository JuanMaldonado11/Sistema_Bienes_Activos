from activos.models import Ciudad,Ubicacion,Establecimiento,EstadoActivo,MarcaActivo,ModeloActivo,TipoBienActivo,Activo
from rest_framework import serializers

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ciudad
        fields=('nombre',)

class EstablecimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model =Establecimiento
        fields=('nombre','direccion','telefono')

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model =Ubicacion
        fields=('nombre',)

class EstadoActivoSerializer(serializers.ModelSerializer):
    class Meta:
        model =EstadoActivo
        fields=('nombre',)

class MarcaActivoSerializer(serializers.ModelSerializer):
    class Meta:
        model= MarcaActivo
        fields=('nombre',)

class ModeloActivoSerializer(serializers.ModelSerializer):
    class Meta:
        model= ModeloActivo
        fields=('nombre',)

class EstadoActivoSerializer(serializers.ModelSerializer):
    class Meta:
        model =EstadoActivo
        fields=('nombre',)

class TipoBienActivoSerializer(serializers.ModelSerializer):
    class Meta:
        model =TipoBienActivo
        fields=('nombre',)

class ActivoSerializer(serializers.ModelSerializer):
    class Meta:
        model =Activo
        fields=('codigo','n_serie','nombre','tipo','modelo','marca','estado','ciudad','establecimiento','ubicacion','delegado','observaciones','mantenimiento','fecha','valor')