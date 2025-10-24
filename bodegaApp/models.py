from django.db import models

# Modelo bodega y vino
class Bodega(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200,verbose_name="Nombre")
    direccion = models.CharField(max_length=300,verbose_name="Dirección") 
    descripcion = models.TextField(verbose_name="Descripción")
    telefono = models.CharField(max_length=20,verbose_name="Teléfono")
    email = models.EmailField(verbose_name="Email")
    ubicacion = models.CharField(max_length=200,verbose_name="Ubicación")
    imagen = models.ImageField(upload_to='imagenes/',verbose_name="Imagen")
    sitio = models.URLField(verbose_name="Sitio web",blank=True)

#Es un método especial de Python que define cómo se muestra el objeto cuando lo convertís a string.
    def __str__(self):  
        return self.nombre
class Vino(models.Model):
    
    # ('valor_guardado_en_bd', 'Texto que ve el usuario')
    CHOICES = [
        ('Tinto', 'Tinto'),
        ('Blanco', 'Blanco'),
        ('Rosado', 'Rosado'),
        ('Espumoso', 'Espumoso'),]
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200,verbose_name="Nombre")
    
    # Esto significa: "Cada Vino pertenece a UNA Bodega, pero una Bodega puede tener MUCHOS Vinos"
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE,verbose_name="Bodega",related_name="vinos")
    tipo = models.CharField(max_length=20,choices=CHOICES,verbose_name="Tipo")
    varietal = models.CharField(max_length=100,verbose_name="Varietal")
    precio = models.DecimalField(max_digits=6, decimal_places=2,verbose_name="Precio")
    descripcion = models.TextField(verbose_name="Descripción")
    imagen = models.ImageField(upload_to='imagenes/',verbose_name="Imagen")
    
    def __str__(self):
        return f"{self.nombre} - {self.bodega.nombre}"
