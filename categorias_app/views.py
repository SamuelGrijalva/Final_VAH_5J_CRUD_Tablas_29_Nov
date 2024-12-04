from django.shortcuts import render, redirect
from .models import Categoria

# Create your views here.
def inicio_vistaCategoria(request):
    lascategorias = Categoria.objects.all()
    return render(request, "gestionarCategoria.html", {"miscategorias": lascategorias})

def registrarCategoria(request):
    id_categoria = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    descripcion = request.POST["txtdescripcion"]
    tipo_categoria = request.POST["txttipo"]
    fecha_creacion = request.POST["datecreacion"]
    estado_categoria = request.POST["txtestado"]
    productos_asociados = request.POST["txtproductos"]

    Categoria.objects.create(
        id_categoria=id_categoria,
        nombre=nombre,
        descripcion=descripcion,
        tipo_categoria=tipo_categoria,
        fecha_creacion=fecha_creacion,
        estado_categoria=estado_categoria,
        productos_asociados=productos_asociados,
    )

    return redirect("categoria")

def seleccionarCategoria(request, codigo):
    categoria = Categoria.objects.get(id_categoria=codigo)
    return render(request, "editarcategoria.html", {"miscategorias": categoria})

def editarCategoria(request):
    id_categoria = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    descripcion = request.POST["txtdescripcion"]
    tipo_categoria = request.POST["txttipo"]
    fecha_creacion = request.POST["datecreacion"]
    estado_categoria = request.POST["txtestado"]
    productos_asociados = request.POST["txtproductos"]

    categoria = Categoria.objects.get(id_categoria=id_categoria)
    categoria.nombre = nombre
    categoria.descripcion = descripcion
    categoria.tipo_categoria = tipo_categoria
    categoria.fecha_creacion = fecha_creacion
    categoria.estado_categoria = estado_categoria
    categoria.productos_asociados = productos_asociados

    categoria.save()
    return redirect("categoria")

def borrarCategoria(request, codigo):
    categoria = Categoria.objects.get(id_categoria=codigo)
    categoria.delete()
    return redirect("categoria")
