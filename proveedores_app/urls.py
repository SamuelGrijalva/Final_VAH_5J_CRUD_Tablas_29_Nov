from django.urls import path
from proveedores_app import views

urlpatterns = [
    path("proveedores", views.inicio_vistaProveedores, name="proveedores"),
    path("registrarProveedor/", views.registrarProveedor, name="registrarProveedor"),
    path("seleccionarProveedor/<codigo>", views.seleccionarProveedor, name="seleccionarProveedor"),
    path("editarProveedor/", views.editarProveedor, name="editarProveedor"),
    path("borrarProveedor/<codigo>", views.borrarProveedor, name="borrarProveedor"),
]
