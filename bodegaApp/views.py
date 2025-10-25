from django.shortcuts import render, redirect
from .models import Bodega, Vino
from .forms import BodegaForm, VinoForm

# Create your views here.
def inicio(request):
    return render(request, 'home.html')

def bodegas_lista(request):
    bodegas = Bodega.objects.all() #Traemos todas las bodegas de la base de datos
    return render(request, 'bodegas.html', {'bodegas': bodegas})

def editar_bodega(request,id):
    bodega_Editada = Bodega.objects.get(id=id)
    # formulario aca
    formulario = BodegaForm(
        request.POST or None, # Datos del formulario enviado (si existe)
        request.FILES or None, # Archivos subidos como imagenes (si existe)
        instance=bodega_Editada) # Registro existente a editar (si se pasa)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('administrar')
    return render(request, 'editar_bodega.html', {'formulario':formulario})

def agregar_bodega(request):
    formulario = BodegaForm(
        request.POST or None, # Datos del formulario enviado (si existe)
        request.FILES or None, # Archivos subidos como imagenes (si existe)
        )
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('administrar')
    return render(request,'agregar_bodega.html', {'formulario':formulario})

def eliminar_bodega(request,id):
    bodega_eliminada = Bodega.objects.get(id=id)
    bodega_eliminada.delete()
    return redirect('administrar')

def bodega_detalle(request,id):
    bodega_por_id = Bodega.objects.get(id=id) #Traemos la bodega con el id recibido
    print(bodega_por_id)
    return render(request, 'bodega_Detalle.html', {'bodega': bodega_por_id})


def vinos_lista(request):
    vinos = Vino.objects.all() #Traemos todos los vinos de la base de datos
    return render(request, 'vinos.html', {'vinos': vinos})

def editar_vino(request,id):
    vino_Editado = Vino.objects.get(id=id)
    # formulario aca
    formulario = VinoForm(
        request.POST or None, # Datos del formulario enviado (si existe)
        request.FILES or None, # Archivos subidos como imagenes (si existe)
        instance=vino_Editado) # Registro existente a editar (si se pasa)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('administrar')
    return render(request, 'editar_vino.html', {'formulario':formulario})

def agregar_vino(request):
    formulario = VinoForm(
        request.POST or None, # Datos del formulario enviado (si existe)
        request.FILES or None, # Archivos subidos como imagenes (si existe)
        )
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('administrar')
    return render(request,'agregar_vino.html', {'formulario':formulario})

def eliminar_vino(request,id):
    vino_eliminado = Vino.objects.get(id=id)
    vino_eliminado.delete()
    return redirect('administrar')

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