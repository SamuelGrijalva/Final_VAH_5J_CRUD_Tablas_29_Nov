from django.urls import path
from productos_app import views

urlpatterns = [
    path("producto", views.inicio_vistaProducto, name="producto"),
    path("registrarProducto/", views.registrarProducto, name="registrarProducto"),
    path("seleccionarProducto/<codigo>", views.seleccionarProducto, name="seleccionarProducto"),
    path("editarProducto/", views.editarProducto, name="editarProducto"),
    path("borrarProducto/<codigo>", views.borrarProducto, name="borrarProducto"),
]
