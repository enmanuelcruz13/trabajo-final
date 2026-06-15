from django.shortcuts import render, get_object_or_404, redirect
from .models import Pelicula
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods


def index(request):
    q = request.GET.get('q', '').strip()
    qs = Pelicula.objects.select_related('genero').all()
    if q:
        qs = qs.filter(titulo__icontains=q) | qs.filter(genero__nombre__icontains=q)

    paginator = Paginator(qs, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'peliculas/index.html', {'page_obj': page_obj, 'q': q})


def detalle(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    return render(request, 'peliculas/detalle.html', {'pelicula': pelicula})


@login_required
def agregar_favorito(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    from .models import Favorito
    Favorito.objects.get_or_create(usuario=request.user, pelicula=pelicula)
    return redirect('detalle', pk=pk)


@require_http_methods(["GET", "POST"])
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if username and password:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect('index')
    return render(request, 'registration/register.html')
