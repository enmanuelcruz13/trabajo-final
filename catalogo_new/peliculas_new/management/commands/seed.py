from django.core.management.base import BaseCommand
from peliculas_new.models import Genero, Pelicula

SAMPLE = [
    ("Accion", [
        ("Velocidad Extrema", "Una pelicula de accion y persecuciones.", 2010),
        ("Mision Imposible", "Agente realiza misiones arriesgadas.", 1996),
    ]),
    ("Comedia", [
        ("Risas Sin Fin", "Comedia familiar para todas las edades.", 2015),
    ]),
]


class Command(BaseCommand):
    help = 'Crea datos de ejemplo (generos y peliculas) para peliculas_new'

    def handle(self, *args, **options):
        self.stdout.write('Creando datos de ejemplo...')
        for genero_name, pelis in SAMPLE:
            genero, _ = Genero.objects.get_or_create(nombre=genero_name)
            for titulo, descripcion, anio in pelis:
                Pelicula.objects.get_or_create(
                    titulo=titulo,
                    defaults={'descripcion': descripcion, 'anio': anio, 'genero': genero}
                )
        self.stdout.write(self.style.SUCCESS('Datos de ejemplo creados.'))
