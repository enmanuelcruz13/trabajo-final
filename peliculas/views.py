from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db import models
from django.db.models import Avg, Count, Case, When, IntegerField, Q
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Pelicula, Favorito, Calificacion, Genero, HistorialVisualizacion
from .forms import PeliculaForm

from .recommender import recomendar, similares
import re


def youtube_to_embed(url):
    """Convierte una URL de YouTube a formato embed."""
    if not url:
        return ''
    match = re.search(r'(?:youtube\.com/watch\?v=|youtu\.be/)([\w-]+)', url)
    if match:
        return f'https://www.youtube.com/embed/{match.group(1)}'
    if 'youtube.com/embed/' in url:
        return url
    return url


@login_required
def index(request):
    q = request.GET.get('q', '').strip()
    genero_id = request.GET.get('genero', '').strip()
    solo_trailers = request.GET.get('trailers') == '1'
    
    qs = Pelicula.objects.annotate(
        promedio_calificacion=Avg('calificaciones__puntuacion'),
        num_calificaciones=Count('calificaciones')
    ).select_related('genero').all()
    
    if solo_trailers:
        qs = qs.exclude(video_url='').exclude(video_url__isnull=True)
    
    if q:
        qs = qs.filter(
            models.Q(titulo__icontains=q) | 
            models.Q(descripcion__icontains=q) | 
            models.Q(genero__nombre__icontains=q)
        )
    if genero_id:
        qs = qs.filter(genero_id=genero_id)
        
    qs = qs.order_by('titulo')
    
    per_page = 100
    paginator = Paginator(qs, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    generos = Genero.objects.all()
    
    favoritos_ids = []
    recientes = []
    recomendadas = []
    if request.user.is_authenticated:
        favoritos_ids = list(Favorito.objects.filter(usuario=request.user).values_list('pelicula_id', flat=True))
        
        vistas_ids = list(HistorialVisualizacion.objects.filter(
            usuario=request.user
        ).order_by('-visto_en').values_list('pelicula_id', flat=True)[:10])
        
        if vistas_ids:
            preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(vistas_ids)], output_field=IntegerField())
            recientes = Pelicula.objects.filter(pk__in=vistas_ids).annotate(
                promedio_calificacion=Avg('calificaciones__puntuacion'),
                num_calificaciones=Count('calificaciones')
            ).select_related('genero').order_by(preserved)
        
        recomendadas = recomendar(request.user, max_results=12)
    return render(request, 'peliculas/index.html', {
        'page_obj': page_obj,
        'generos': generos,
        'favoritos_ids': favoritos_ids,
        'recientes': recientes,
        'recomendadas': recomendadas,
        'q': q,
        'selected_genero': genero_id,
        'solo_trailers': solo_trailers,
    })


@login_required
def detalle(request, pk):
    try:
        pelicula = Pelicula.objects.annotate(
            promedio_calificacion=Avg('calificaciones__puntuacion'),
            num_calificaciones=Count('calificaciones')
        ).get(pk=pk)
    except Pelicula.DoesNotExist:
        messages.error(request, 'La pelicula solicitada no existe.')
        return redirect('peliculas:index')
    
    is_favorito = False
    mi_calificacion = None
    if request.user.is_authenticated:
        is_favorito = Favorito.objects.filter(usuario=request.user, pelicula=pelicula).exists()
        calif = Calificacion.objects.filter(usuario=request.user, pelicula=pelicula).first()
        if calif:
            mi_calificacion = calif.puntuacion
        HistorialVisualizacion.objects.update_or_create(
            usuario=request.user,
            pelicula=pelicula,
            defaults={'visto_en': timezone.now()}
        )
            
    favoritos_ids = []
    if request.user.is_authenticated:
        favoritos_ids = list(Favorito.objects.filter(usuario=request.user).values_list('pelicula_id', flat=True))
    
    # Always use seed video as baseline
    video_id = pelicula.get_youtube_id()

    def build_video(vid, title_override=None):
        if not vid:
            return None
        return {
            'video_id': vid,
            'title': title_override or pelicula.titulo,
            'thumbnail': f'https://img.youtube.com/vi/{vid}/mqdefault.jpg',
            'watch_url': f'https://www.youtube.com/watch?v={vid}',
        }

    # Use seed video directly (YouTube API quota is exceeded)
    main_video = build_video(video_id) if video_id else None
    secondary_video = None
        
    peliculas_similares = similares(pelicula, max_results=6)

    return render(request, 'peliculas/detalle.html', {
        'pelicula': pelicula,
        'is_favorito': is_favorito,
        'favoritos_ids': favoritos_ids,
        'mi_calificacion': mi_calificacion,
        'main_video': main_video,
        'secondary_video': secondary_video,
        'peliculas_similares': peliculas_similares,
    })


@login_required
def toggle_favorito(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    fav, created = Favorito.objects.get_or_create(usuario=request.user, pelicula=pelicula)
    if not created:
        fav.delete()
        favorited = False
    else:
        favorited = True

    is_ajax = (request.headers.get('x-requested-with') == 'XMLHttpRequest' or 
               'application/json' in request.headers.get('accept', ''))
    if is_ajax:
        return JsonResponse({'favorited': favorited})

    referer = request.META.get('HTTP_REFERER')
    return redirect(referer if referer else 'peliculas:index')


@login_required
def calificar_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    if request.method == 'POST':
        try:
            import json
            if request.headers.get('content-type') == 'application/json':
                data = json.loads(request.body)
                puntuacion = int(data.get('puntuacion'))
            else:
                puntuacion = int(request.POST.get('puntuacion'))
            
            if 1 <= puntuacion <= 5:
                calif, created = Calificacion.objects.update_or_create(
                    usuario=request.user,
                    pelicula=pelicula,
                    defaults={'puntuacion': puntuacion}
                )
                
                stats = Calificacion.objects.filter(pelicula=pelicula).aggregate(
                    promedio=Avg('puntuacion'),
                    total=Count('id')
                )
                
                is_ajax = (request.headers.get('x-requested-with') == 'XMLHttpRequest' or 
                           'application/json' in request.headers.get('accept', ''))
                if is_ajax:
                    return JsonResponse({
                        'success': True,
                        'promedio': round(stats['promedio'], 1) if stats['promedio'] else 0,
                        'total': stats['total'],
                        'mi_calificacion': calif.puntuacion
                    })
            else:
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({'success': False, 'error': 'Calificación inválida'})
        except Exception as e:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'error': str(e)})
                
    return redirect('peliculas:detalle', pk=pk)


@login_required
def mis_favoritos(request):
    favs = Favorito.objects.filter(usuario=request.user).select_related('pelicula')
    pelicula_ids = [f.pelicula_id for f in favs]
    
    peliculas = Pelicula.objects.filter(id__in=pelicula_ids).annotate(
        promedio_calificacion=Avg('calificaciones__puntuacion'),
        num_calificaciones=Count('calificaciones')
    ).select_related('genero')
    
    favoritos_ids = list(pelicula_ids)
    
    return render(request, 'peliculas/mis_favoritos.html', {
        'peliculas': peliculas,
        'favoritos_ids': favoritos_ids
    })


@login_required
def agregar_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            pelicula = form.save()
            return redirect('peliculas:detalle', pk=pelicula.pk)
    else:
        form = PeliculaForm()
    return render(request, 'peliculas/agregar.html', {'form': form})
