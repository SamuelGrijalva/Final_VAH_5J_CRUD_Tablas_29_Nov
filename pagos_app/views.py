from django.shortcuts import render, redirect
from .models import Pago

# Create your views here.
def inicio_vistaPago(request):
    lospagos = Pago.objects.all()
    return render(request, "gestionarPago.html", {"mispagos": lospagos})

def registrarPago(request):
    id_pago = request.POST["txtcodigo"]
    id_pedidos = request.POST["txtpedidos"]
    fecha_pago = request.POST["datepago"]
    monto = request.POST["txtmonto"]
    metodo_pago = request.POST["txtmetodo"]
    estado_pago = request.POST["txtestado"]
    transaccion = request.POST["txttransaccion"]

    Pago.objects.create(
        id_pago=id_pago,
        id_pedidos=id_pedidos,
        fecha_pago=fecha_pago,
        monto=monto,
        metodo_pago=metodo_pago,
        estado_pago=estado_pago,
        transaccion=transaccion,
    )

    return redirect("pago")

def seleccionarPago(request, codigo):
    pago = Pago.objects.get(id_pago=codigo)
    fecha_pago=pago.fecha_pago.strftime('%Y-%m-%d')
    return render(request,"editarpago.html",{"mispagos":pago, "mispagos" : pago, "fecha_pago" : fecha_pago})

def editarPago(request):
    id_pago = request.POST["txtcodigo"]
    id_pedidos = request.POST["txtpedidos"]
    fecha_pago = request.POST["datepago"]
    monto = request.POST["txtmonto"]
    metodo_pago = request.POST["txtmetodo"]
    estado_pago = request.POST["txtestado"]
    transaccion = request.POST["txttransaccion"]

    pago = Pago.objects.get(id_pago=id_pago)
    pago.id_pedidos = id_pedidos
    pago.fecha_pago = fecha_pago
    pago.monto = monto
    pago.metodo_pago = metodo_pago
    pago.estado_pago = estado_pago
    pago.transaccion = transaccion

    pago.save()
    return redirect("pago")

def borrarPago(request, codigo):
    pago = Pago.objects.get(id_pago=codigo)
    pago.delete()
    return redirect("pago")
