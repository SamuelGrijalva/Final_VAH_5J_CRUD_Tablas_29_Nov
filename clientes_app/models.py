from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente=models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=50)
    telefono = models.PositiveIntegerField()
    direccion = models.CharField(max_length=100)
    fecha_registro = models.DateField(null=False,blank=False)
    tipo_cliente = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre