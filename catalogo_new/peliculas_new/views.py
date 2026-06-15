from django.shortcuts import render, get_object_or_404
from .models import Pelicula


def index(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'peliculas_new/index.html', {'peliculas': peliculas})


def detalle(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    return render(request, 'peliculas_new/detalle.html', {'pelicula': pelicula})
