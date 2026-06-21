import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "catalogo.settings")
django.setup()

from peliculas.models import Pelicula

total = Pelicula.objects.count()
pelis = Pelicula.objects.filter(tipo="pelicula").count()
series = Pelicula.objects.filter(tipo="serie").count()
trailers = Pelicula.objects.exclude(video_url="").exclude(video_url__isnull=True).count()

print(f"Total: {total}")
print(f"Peliculas: {pelis}")
print(f"Series: {series}")
print(f"Con trailer: {trailers}")
