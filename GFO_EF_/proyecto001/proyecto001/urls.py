from django.contrib import admin
from django.urls import path
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.inicio, name="index"),
    path("inicio/", views.inicio, name="inicio"),
    path("integrantes/", views.integrantes, name="integrantes"),
    path("crearDocente/", views.crearDocente, name="crearDocente"),
    path("guardarDocente/", views.guardarDocente, name="guardarDocente"),
    path("listarDocentes/", views.listarDocentes, name="listarDocentes"),
    path("crearCurso/", views.crearCurso, name="crearCurso"),
    path("listarCursos/", views.listarCursos, name="listarCursos"),
    path("eliminarDocente/<int:id>", views.eliminarDocente, name="eliminarDocente")
]