from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'home.html')

def bodegas(request):
    return render(request, 'bodegas.html')

def vinos(request):
    return render(request, 'vinos.html')

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