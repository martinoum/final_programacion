from django.shortcuts import render
from .models import Bodega, Vino
# Create your views here.
def inicio(request):
    return render(request, 'home.html')

def bodegas_lista(request):
    bodegas = Bodega.objects.all() #Traemos todas las bodegas de la base de datos
    return render(request, 'bodegas.html', {'bodegas': bodegas})

def vinos_lista(request):
    vinos = Vino.objects.all() #Traemos todos los vinos de la base de datos
    return render(request, 'vinos.html', {'vinos': vinos})

def bodega_detalle(request):
    return render(request, 'bodega_Detalle.html')

def vino_detalle(request):
    return render(request, 'vino_Detalle.html')

def administrar(request):
    return render(request, 'administrar.html')

def formulario_bodega(request):
    return render(request, 'bodega_form.html')

def formulario_vino(request):
    return render(request, 'vino_form.html')

def about(request):
    return render(request, 'about.html')