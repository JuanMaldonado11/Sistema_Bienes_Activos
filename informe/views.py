from django.shortcuts import render
from django.http import HttpResponse
from informe.models import Informe
from rest_framework import viewsets
from informe.serializers import InformeSerializer


class InformeViewSet(viewsets.ModelViewSet):
    queryset=Informe.objects.all().order_by('codigo_acta')
    serializer_class=InformeSerializer
# Create your views here.
def index (request):
    return HttpResponse("Pagina de informe")
