from django.db import models

# Create your models here.
class Pago(models.Model):
    id_pago=models.PositiveIntegerField(primary_key=True)
    id_pedidos=models.PositiveIntegerField()
    fecha_pago = models.DateField(null=False,blank=False)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    estado_pago = models.CharField(max_length=50)
    transaccion = models.CharField(max_length=100)

    def __str__(self):
        return self.id_pago