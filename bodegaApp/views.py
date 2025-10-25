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

def bodega_detalle(request,id):
    bodega_por_id = Bodega.objects.get(id=id) #Traemos la bodega con el id recibido
    print(bodega_por_id)
    return render(request, 'bodega_Detalle.html', {'bodega': bodega_por_id})

def vino_detalle(request,id):
    vino_por_id = Vino.objects.get(id=id) #Traemos el vino con el id recibido
    print(vino_por_id)
    return render(request, 'vino_Detalle.html', {'vino': vino_por_id})

def administrar(request):
    bodegas = Bodega.objects.all()
    vinos = Vino.objects.all()
    return render(request, 'administrar.html', {'bodegas': bodegas, 'vinos': vinos})

def formulario_bodega(request):
    return render(request, 'bodega_form.html')

def formulario_vino(request):
    return render(request, 'vino_form.html')

def about(request):
    return render(request, 'about.html')