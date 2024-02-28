from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def index (request):
    contextos = {
        'title': "Pagina Inicio",
    }
    return render(request,'activos/activos_index.html', contextos)