from django.shortcuts import render, redirect
from .models import Inscripcion
from .forms import FormInscripcion

def index(request):
    return render(request, 'index.html')

def listaInscripciones(request):
    inscripciones = Inscripcion.objects.all()
    return render(request, 'ListarInscripciones.html', {'inscripciones': inscripciones})

def agregarInscripcion(request):
    form = FormInscripcion()
    if request.method == 'POST':
        form = FormInscripcion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_inscripciones')
    return render(request, 'agregarInscripcion.html', {'form': form})

def modificarInscripcion(request, id):
    inscripcion = Inscripcion.objects.get(id=id)
    form = FormInscripcion(instance=inscripcion)
    if request.method == 'POST':
        form = FormInscripcion(request.POST, instance=inscripcion)
        if form.is_valid():
            form.save()
            return redirect('listar_inscripciones')
    return render(request, 'modificarInscripcion.html', {'form': form})

def eliminarInscripcion(request, id):
    inscripcion = Inscripcion.objects.get(id=id)
    inscripcion.delete()
    return redirect('listar_inscripciones')
