from django.db import models

# Create your models here.
class Proveedor(models.Model):
    id_proveedor=models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    telefono = models.PositiveIntegerField()
    correo = models.EmailField(max_length=50)
    direccion = models.CharField(max_length=300)
    fecha_registro = models.DateField(null=False,blank=False)

    def __str__(self):
        return self.nombre