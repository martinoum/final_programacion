"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bodegaApp.views import formulario_vino, inicio, bodegas, vinos, bodega_detalle, vino_detalle, administrar, formulario_bodega

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('bodegas/', bodegas, name='bodegas'),
    path('vinos/',vinos, name='vinos'),
    path('bodega/detalle', bodega_detalle, name='bodega_detalle'),
    path('vino/detalle', vino_detalle, name='vino_detalle'),
    path('administrar/', administrar, name='administrar'),
    path('bodega/formulario/', formulario_bodega, name='formulario_bodega'),
    path('vino/formulario/', formulario_vino, name='formulario_vino'),
]
