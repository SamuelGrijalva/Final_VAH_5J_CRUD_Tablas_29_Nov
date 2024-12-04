from django.shortcuts import render, redirect
from .models import Cliente

def inicio_vistaClientes(request):
    los_clientes = Cliente.objects.all()
    return render(request, "gestionarCliente.html", {"mis_clientes": los_clientes})

def registrarCliente(request):
    id_cliente = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    correo = request.POST["txtcorreo"]
    telefono = request.POST["txttelefono"]
    direccion = request.POST["txtdireccion"]
    fecha_registro = request.POST["txtfecha"]
    tipo_cliente = request.POST["txttipo"]

    Cliente.objects.create(
        id_cliente=id_cliente,
        nombre=nombre,
        correo=correo,
        telefono=telefono,
        direccion=direccion,
        fecha_registro=fecha_registro,
        tipo_cliente=tipo_cliente,
    )
    return redirect("clientes")

def seleccionarCliente(request, codigo):
    cliente = Cliente.objects.get(id_cliente=codigo)
    fecha_registro=cliente.fecha_registro.strftime('%Y-%m-%d')
    return render(request,"editarCliente.html",{"mi_cliente":cliente, "mi_cliente" : cliente, "fecha_registro" : fecha_registro})

def editarCliente(request):
    id_cliente = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    correo = request.POST["txtcorreo"]
    telefono = request.POST["txttelefono"]
    direccion = request.POST["txtdireccion"]
    fecha_registro = request.POST["txtfecha"]
    tipo_cliente = request.POST["txttipo"]

    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.nombre = nombre
    cliente.correo = correo
    cliente.telefono = telefono
    cliente.direccion = direccion
    cliente.fecha_registro = fecha_registro
    cliente.tipo_cliente = tipo_cliente
    cliente.save()
    return redirect("clientes")

def borrarCliente(request, codigo):
    cliente = Cliente.objects.get(id_cliente=codigo)
    cliente.delete()
    return redirect("clientes")
