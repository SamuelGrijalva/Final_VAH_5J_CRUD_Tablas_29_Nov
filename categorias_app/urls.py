from django.urls import path
from categorias_app import views

urlpatterns = [
    path("categoria", views.inicio_vistaCategoria, name="categoria"),
    path("registrarCategoria/", views.registrarCategoria, name="registrarCategoria"),
    path("seleccionarCategoria/<codigo>", views.seleccionarCategoria, name="seleccionarCategoria"),
    path("editarCategoria/", views.editarCategoria, name="editarCategoria"),
    path("borrarCategoria/<codigo>", views.borrarCategoria, name="borrarCategoria"),
]
