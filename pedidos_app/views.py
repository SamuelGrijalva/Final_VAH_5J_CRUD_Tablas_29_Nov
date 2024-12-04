from django.shortcuts import render, redirect
from .models import Pedido

def inicio_vistaPedidos(request):
    los_pedidos = Pedido.objects.all()
    return render(request, "gestionarPedido.html", {"mis_pedidos": los_pedidos})

def registrarPedido(request):
    id_pedido = request.POST["txtcodigo"]
    id_cliente = request.POST["txtcliente"]
    fecha_pedido = request.POST["txtfecha"]
    total = request.POST["txttotal"]
    estado = request.POST["txtestado"]
    metodo_pago = request.POST["txtmetodo"]
    direccion_envio = request.POST["txtdireccion"]

    Pedido.objects.create(
        id_pedido=id_pedido,
        id_cliente=id_cliente,
        fecha_pedido=fecha_pedido,
        total=total,
        estado=estado,
        metodo_pago=metodo_pago,
        direccion_envio=direccion_envio,
    )
    return redirect("pedidos")

def seleccionarPedido(request, codigo):
    pedido = Pedido.objects.get(id_pedido=codigo)
    fecha_pedido=pedido.fecha_pedido.strftime('%Y-%m-%d')
    return render(request,"editarPedido.html",{"mi_pedido":pedido, "mi_pedido" : pedido, "fecha_pedido" : fecha_pedido})

def editarPedido(request):
    id_pedido = request.POST["txtcodigo"]
    id_cliente = request.POST["txtcliente"]
    fecha_pedido = request.POST["txtfecha"]
    total = request.POST["txttotal"]
    estado = request.POST["txtestado"]
    metodo_pago = request.POST["txtmetodo"]
    direccion_envio = request.POST["txtdireccion"]

    pedido = Pedido.objects.get(id_pedido=id_pedido)
    pedido.id_cliente = id_cliente
    pedido.fecha_pedido = fecha_pedido
    pedido.total = total
    pedido.estado = estado
    pedido.metodo_pago = metodo_pago
    pedido.direccion_envio = direccion_envio
    pedido.save()
    return redirect("pedidos")

def borrarPedido(request, codigo):
    pedido = Pedido.objects.get(id_pedido=codigo)
    pedido.delete()
    return redirect("pedidos")
