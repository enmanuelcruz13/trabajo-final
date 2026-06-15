from django.shortcuts import render, get_object_or_404, redirect
from .models import Pelicula
from django.contrib.auth.decorators import login_required

def index(request):
    peliculas = Pelicula.objects.select_related('genero').all()[:50]
    return render(request, 'peliculas/index.html', {'peliculas': peliculas})

def detalle(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    return render(request, 'peliculas/detalle.html', {'pelicula': pelicula})

@login_required
def agregar_favorito(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    from .models import Favorito
    Favorito.objects.get_or_create(usuario=request.user, pelicula=pelicula)
    return redirect('detalle', pk=pk)
