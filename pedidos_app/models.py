from django.db import models

# Create your models here.
class Pedido(models.Model):
    id_pedido=models.PositiveIntegerField(primary_key=True)
    id_cliente=models.PositiveIntegerField()
    fecha_pedido = models.DateField(null=False,blank=False)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=50)
    metodo_pago = models.CharField(max_length=50)
    direccion_envio = models.CharField(max_length=200)

    def __str__(self):
        return self.id_cliente