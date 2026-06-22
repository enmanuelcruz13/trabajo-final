from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from django.db.models import Avg, Count, Case, When, IntegerField
from .models import Pelicula


def _annotate(qs):
    return qs.annotate(
        promedio_calificacion=Avg('calificaciones__puntuacion'),
        num_calificaciones=Count('calificaciones')
    ).select_related('genero')


def recomendar(user, max_results=12):
    historial = list(user.historialvisualizacion_set.values_list('pelicula_id', flat=True))
    ratings_qs = user.calificacion_set.all()
    ratings = {r.pelicula_id: r.puntuacion for r in ratings_qs}
    ids_conocidos = set(historial) | set(ratings.keys())

    if not ids_conocidos:
        return _annotate(Pelicula.objects.all()).order_by('-promedio_calificacion')[:max_results]

    peliculas = list(Pelicula.objects.select_related('genero').all())
    if not peliculas:
        return []

    idx_map = {p.id: i for i, p in enumerate(peliculas)}
    docs = [
        ' '.join([p.titulo, p.descripcion or '', p.genero.nombre if p.genero else ''])
        for p in peliculas
    ]

    vectorizer = TfidfVectorizer(stop_words='spanish', max_features=1000)
    matrix = vectorizer.fit_transform(docs)

    user_vector = np.zeros(matrix.shape[1])
    total_peso = 0
    for pid in ids_conocidos:
        if pid in idx_map:
            i = idx_map[pid]
            w = (ratings.get(pid, 3) - 3) / 2
            user_vector += matrix[i].toarray().flatten() * w
            total_peso += abs(w)

    if total_peso > 0:
        user_vector /= total_peso
    else:
        return _annotate(Pelicula.objects.all()).order_by('-promedio_calificacion')[:max_results]

    sims = cosine_similarity(user_vector.reshape(1, -1), matrix).flatten()
    for pid in ids_conocidos:
        if pid in idx_map:
            sims[idx_map[pid]] = -1

    top_indices = np.argsort(sims)[::-1][:max_results]
    ids_recomendadas = [peliculas[i].id for i in top_indices if sims[i] > 0]

    if ids_recomendadas:
        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids_recomendadas)], output_field=IntegerField())
        return _annotate(Pelicula.objects.filter(pk__in=ids_recomendadas)).order_by(preserved)
    return _annotate(Pelicula.objects.all()).order_by('-promedio_calificacion')[:max_results]
