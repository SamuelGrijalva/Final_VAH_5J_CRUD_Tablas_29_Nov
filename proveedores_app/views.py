from django.shortcuts import render, redirect
from .models import Proveedor

def inicio_vistaProveedores(request):
    los_proveedores = Proveedor.objects.all()
    return render(request, "gestionarProveedor.html", {"mis_proveedores": los_proveedores})

def registrarProveedor(request):
    id_proveedor = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    contacto = request.POST["txtcontacto"]
    telefono = request.POST["txttelefono"]
    correo = request.POST["txtcorreo"]
    direccion = request.POST["txtdireccion"]
    fecha_registro = request.POST["txtfecha"]

    Proveedor.objects.create(
        id_proveedor=id_proveedor,
        nombre=nombre,
        contacto=contacto,
        telefono=telefono,
        correo=correo,
        direccion=direccion,
        fecha_registro=fecha_registro,
    )
    return redirect("proveedores")

def seleccionarProveedor(request, codigo):
    proveedor = Proveedor.objects.get(id_proveedor=codigo)
    fecha_registro=proveedor.fecha_registro.strftime('%Y-%m-%d')
    return render(request,"editarProveedor.html",{"mi_proveedor":proveedor, "mi_proveedor" : proveedor, "fecha_registro" : fecha_registro})

def editarProveedor(request):
    id_proveedor = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    contacto = request.POST["txtcontacto"]
    telefono = request.POST["txttelefono"]
    correo = request.POST["txtcorreo"]
    direccion = request.POST["txtdireccion"]
    fecha_registro = request.POST["txtfecha"]

    proveedor = Proveedor.objects.get(id_proveedor=id_proveedor)
    proveedor.nombre = nombre
    proveedor.contacto = contacto
    proveedor.telefono = telefono
    proveedor.correo = correo
    proveedor.direccion = direccion
    proveedor.fecha_registro = fecha_registro
    proveedor.save()
    return redirect("proveedores")

def borrarProveedor(request, codigo):
    proveedor = Proveedor.objects.get(id_proveedor=codigo)
    proveedor.delete()
    return redirect("proveedores")
