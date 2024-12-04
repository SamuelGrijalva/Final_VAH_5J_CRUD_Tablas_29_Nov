from django.urls import path
from pagos_app import views

urlpatterns = [
    path("pago", views.inicio_vistaPago, name="pago"),
    path("registrarPago/", views.registrarPago, name="registrarPago"),
    path("seleccionarPago/<codigo>", views.seleccionarPago, name="seleccionarPago"),
    path("editarPago/", views.editarPago, name="editarPago"),
    path("borrarPago/<codigo>", views.borrarPago, name="borrarPago"),
]
