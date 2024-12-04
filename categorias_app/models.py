from django.db import models

# Create your models here.
class Categoria(models.Model):
    id_categoria=models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    tipo_categoria = models.CharField(max_length=50)
    fecha_creacion = models.DateField(null=False,blank=False)
    estado_categoria = models.CharField(max_length=50)
    productos_asociados = models.CharField(max_length=300)

    def __str__(self):
        return self.nombre