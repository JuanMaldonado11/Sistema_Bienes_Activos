from informe.models import Informe
from rest_framework import serializers

class InformeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Informe
        fields=('nombre_tipobienactivo','activo','revisor','director','codigo_acta','informe','fecha')