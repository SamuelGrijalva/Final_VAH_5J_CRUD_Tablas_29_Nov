from django.urls import path
from pedidos_app import views

urlpatterns = [
    path("pedidos", views.inicio_vistaPedidos, name="pedidos"),
    path("registrarPedido/", views.registrarPedido, name="registrarPedido"),
    path("seleccionarPedido/<codigo>", views.seleccionarPedido, name="seleccionarPedido"),
    path("editarPedido/", views.editarPedido, name="editarPedido"),
    path("borrarPedido/<codigo>", views.borrarPedido, name="borrarPedido"),
]
