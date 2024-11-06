from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar/', views.agregarInscripcion, name='agregar_inscripcion'),
    path('listar/', views.listaInscripciones, name='listar_inscripciones'),
    path('modificar/<int:id>/', views.modificarInscripcion, name='modificar_inscripcion'),
    path('eliminar/<int:id>/', views.eliminarInscripcion, name='eliminar_inscripcion'),
]
