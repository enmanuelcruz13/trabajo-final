import django
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'catalogo.settings'
django.setup()
from peliculas.models import Pelicula
for p in Pelicula.objects.all().order_by('titulo'):
    status = "SI" if p.video_url else "NO"
    print(f"{p.titulo}: {status}")
