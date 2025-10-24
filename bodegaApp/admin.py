from django.contrib import admin
from .models import Bodega, Vino

# Registrmos los modelos para que aparezcan en el admin de Django

@admin.register(Bodega)
class BodegaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'direccion','descripcion','telefono','email','ubicacion','imagen','sitio')
    
@admin.register(Vino)
class VinoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'bodega', 'tipo', 'varietal', 'precio', 'descripcion', 'imagen')
