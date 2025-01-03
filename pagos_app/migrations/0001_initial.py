# Generated by Django 5.1.3 on 2024-12-04 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id_pago', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('id_pedidos', models.PositiveIntegerField()),
                ('fecha_pago', models.DateField()),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('metodo_pago', models.CharField(max_length=50)),
                ('estado_pago', models.CharField(max_length=50)),
                ('transaccion', models.CharField(max_length=100)),
            ],
        ),
    ]
