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
from bodegaApp.views import about, formulario_vino, inicio, bodegas_lista, vinos_lista, bodega_detalle, vino_detalle, administrar, formulario_bodega

from django.conf import settings #PENDIENTE notion
from django.contrib.staticfiles.urls import static #PENDIENTE notion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('bodegas_lista/', bodegas_lista, name='bodegas_lista'),
    path('vinos_lista/', vinos_lista, name='vinos_lista'),
    path('bodega/detalle', bodega_detalle, name='bodega_detalle'),
    path('vino/detalle', vino_detalle, name='vino_detalle'),
    path('administrar/', administrar, name='administrar'),
    path('bodega/formulario/', formulario_bodega, name='formulario_bodega'),
    path('vino/formulario/', formulario_vino, name='formulario_vino'),
    path('about/', about, name='about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #PENDIENTE notion
