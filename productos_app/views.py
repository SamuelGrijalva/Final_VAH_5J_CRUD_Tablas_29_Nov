from django.shortcuts import render, redirect
from .models import Producto

# Create your views here.
def inicio_vistaProducto(request):
    losproductos = Producto.objects.all()
    return render(request, "gestionarProducto.html", {"misproductos": losproductos})

def registrarProducto(request):
    id_producto = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    descripcion = request.POST["txtdescripcion"]
    precio = request.POST["txtprecio"]
    stock = request.POST["txtstock"]
    id_categoria = request.POST["txtcategoria"]
    id_proveedor = request.POST["txtproveedor"]

    Producto.objects.create(
        id_producto=id_producto,
        nombre=nombre,
        descripcion=descripcion,
        precio=precio,
        stock=stock,
        id_categoria=id_categoria,
        id_proveedor=id_proveedor,
    )

    return redirect("producto")

def seleccionarProducto(request, codigo):
    producto = Producto.objects.get(id_producto=codigo)
    return render(request, "editarproducto.html", {"misproductos": producto})

def editarProducto(request):
    id_producto = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    descripcion = request.POST["txtdescripcion"]
    precio = request.POST["txtprecio"]
    stock = request.POST["txtstock"]
    id_categoria = request.POST["txtcategoria"]
    id_proveedor = request.POST["txtproveedor"]

    producto = Producto.objects.get(id_producto=id_producto)
    producto.nombre = nombre
    producto.descripcion = descripcion
    producto.precio = precio
    producto.stock = stock
    producto.id_categoria = id_categoria
    producto.id_proveedor = id_proveedor

    producto.save()
    return redirect("producto")

def borrarProducto(request, codigo):
    producto = Producto.objects.get(id_producto=codigo)
    producto.delete()
    return redirect("producto")
