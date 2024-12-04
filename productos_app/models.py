from django.db import models

# Create your models here.
class Producto(models.Model):
    id_producto=models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    id_categoria = models.PositiveIntegerField()
    id_proveedor = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre