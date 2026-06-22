#!/usr/bin/env python
"""
Poblar BD con peliculas exclusivas de 2014-2026 en distintas categorias.
"""
from django.core.management.base import BaseCommand
from peliculas.models import Genero, Pelicula

PELICULAS = [
    # Accion
    {'titulo': 'Mad Max: Fury Road', 'descripcion': 'En un futuro distopico, Max se une a una rebelion para cruzar el desierto.', 'anio': 2015, 'genero': 'Accion', 'imagen': 'https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg', 'video_url': 'https://www.youtube.com/watch?v=34jggoc78YQ'},
    {'titulo': 'John Wick', 'descripcion': 'Un exasesino sale del retiro para vengar la muerte de su perro.', 'anio': 2014, 'genero': 'Accion', 'imagen': 'https://upload.wikimedia.org/wikipedia/en/9/98/John_Wick_TeaserPoster.jpg', 'video_url': 'https://www.youtube.com/watch?v=JqbaroodoMY'},
    {'titulo': 'Mission: Impossible - Fallout', 'descripcion': 'Ethan Hunt debe detener una amenaza nuclear antes de que sea demasiado tarde.', 'anio': 2018, 'genero': 'Accion', 'imagen': 'https://upload.wikimedia.org/wikipedia/en/f/ff/MI_%E2%80%93_Fallout.jpg', 'video_url': 'https://www.youtube.com/watch?v=gPf-JzvmZ7k'},
    {'titulo': 'The Equalizer', 'descripcion': 'Un hombre con un pasado letal ayuda a una joven en problemas.', 'anio': 2014, 'genero': 'Accion', 'imagen': 'https://upload.wikimedia.org/wikipedia/en/8/81/The_Equalizer_poster.jpg', 'video_url': 'https://www.youtube.com/watch?v=VjctHUEmutw'},
    # Drama
    {'titulo': 'Whiplash', 'descripcion': 'Un joven baterista lucha por la perfeccion bajo un instructor despiadado.', 'anio': 2014, 'genero': 'Drama', 'imagen': 'https://upload.wikimedia.org/wikipedia/en/0/01/Whiplash_poster.jpg', 'video_url': 'https://www.youtube.com/watch?v=ZdamZzFQ_nQ'},
    {'titulo': 'The Revenant', 'descripcion': 'Un trampero lucha por sobrevivir en la naturaleza salvaje despues de un ataque.', 'anio': 2015, 'genero': 'Drama', 'imagen': 'https://upload.wikimedia.org/wikipedia/en/b/b6/The_Revenant_2015_film_poster.jpg', 'video_url': 'https://www.youtube.com/watch?v=VTZGlOALm7c'},
    {'titulo': 'Moonlight', 'descripcion': 'La vida de un joven negro gay en Miami desde la infancia hasta la adultez.', 'anio': 2016, 'genero': 'Drama', 'imagen': 'https://upload.wikimedia.org/wikipedia/en/8/84/Moonlight_%282016_film%29.png', 'video_url': 'https://www.youtube.com/watch?v=9NJj12tJzqc'},
    {'titulo': 'Parasite', 'descripcion': 'Una familia pobre se infiltra en la vida de una familia rica con consecuencias inesperadas.', 'anio': 2019, 'genero': 'Drama', 'imagen': 'https://upload.wikimedia.org/wikipedia/en/5/53/Parasite_%282019_film%29.png', 'video_url': 'https://www.youtube.com/watch?v=90dWVETAdtI'},
    {'titulo': 'Oppenheimer', 'descripcion': 'La historia del fisico que lidero el desarrollo de la bomba atomica.', 'anio': 2023, 'genero': 'Drama', 'imagen': 'https://upload.wikimedia.org/wikipedia/en/4/4a/Oppenheimer_%28film%29.jpg', 'video_url': 'https://www.youtube.com/watch?v=JpUd4BS7yI0'},
    # Comedia
    {'titulo': 'The Grand Budapest Hotel', 'descripcion': 'Las aventuras de un conserje y su aprendiz en un famoso hotel europeo.', 'anio': 2014, 'genero': 'Comedia', 'imagen': 'https://upload.wikimedia.org/wikipedia/en/1/1c/The_Grand_Budapest_Hotel.png', 'video_url': 'https://www.youtube.com/watch?v=IImKsmIZ1VY'},
    {'titulo': 'Deadpool', 'descripcion': 'Un mercenario con un sentido del humor retorcido busca venganza.', 'anio': 2016, 'genero': 'Comedia', 'imagen': 'https://upload.wikimedia.org/wikipedia/en/2/23/Deadpool_%282016_poster%29.png', 'video_url': 'https://www.youtube.com/watch?v=vhJroWmp_k8'},
    {'titulo': 'Everything Everywhere All at Once', 'descripcion': 'Una migrante china descubre que puede acceder a realidades paralelas.', 'anio': 2022, 'genero': 'Comedia', 'imagen': 'https://upload.wikimedia.org/wikipedia/en/1/1e/Everything_Everywhere_All_at_Once.jpg', 'video_url': 'https://www.youtube.com/watch?v=wxN1T1uxQ2g'},
    {'titulo': 'Barbie', 'descripcion': 'Barbie y Ken viajan al mundo real y descubren lo que significa ser humano.', 'anio': 2023, 'genero': 'Comedia', 'imagen': 'https://upload.wikimedia.org/wikipedia/en/0/0b/Barbie_2023_poster.jpg', 'video_url': 'https://www.youtube.com/watch?v=zh4KhVSMwtQ'},
    # Ciencia Ficcion
    {'titulo': 'Interstellar', 'descripcion': 'Un equipo de astronautas viaja a traves de un agujero de gusano en busca de un nuevo hogar.', 'anio': 2014, 'genero': 'Ciencia Ficcion', 'imagen': 'https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg', 'video_url': 'https://www.youtube.com/watch?v=JxdU76YYeMc'},
    {'titulo': 'The Martian', 'descripcion': 'Un astronauta varado en Marte lucha por sobrevivir hasta que llegue el rescate.', 'anio': 2015, 'genero': 'Ciencia Ficcion', 'imagen': 'https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg', 'video_url': 'https://www.youtube.com/watch?v=xO-YDwxhMYE'},
    {'titulo': 'Arrival', 'descripcion': 'Una linguista intenta comunicarse con extraterrestres para evitar una guerra.', 'anio': 2016, 'genero': 'Ciencia Ficcion', 'imagen': 'https://upload.wikimedia.org/wikipedia/en/d/df/Arrival%2C_Movie_Poster.jpg', 'video_url': 'https://www.youtube.com/watch?v=FFqmwnkkRtE'},
    {'titulo': 'Dune', 'descripcion': 'Un joven debe viajar a un planeta desertico para salvar el futuro de su familia.', 'anio': 2021, 'genero': 'Ciencia Ficcion', 'imagen': 'https://upload.wikimedia.org/wikipedia/en/8/8e/Dune_%282021_film%29.jpg', 'video_url': 'https://www.youtube.com/watch?v=VzI7Np0hWTY'},
    # Animacion
    {'titulo': 'Inside Out', 'descripcion': 'Las emociones de una nina trabajan juntas para ayudarla a adaptarse a una nueva ciudad.', 'anio': 2015, 'genero': 'Animacion', 'imagen': 'https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg', 'video_url': 'https://www.youtube.com/watch?v=x-xlkjPwaOY'},
    {'titulo': 'Coco', 'descripcion': 'Un joven musico descubre los secretos de su familia en el mundo de los muertos.', 'anio': 2017, 'genero': 'Animacion', 'imagen': 'https://upload.wikimedia.org/wikipedia/en/9/98/Coco_%282017_film%29_poster.jpg', 'video_url': 'https://www.youtube.com/watch?v=Vsx5yHIxn38'},
    {'titulo': 'Spider-Man: Into the Spider-Verse', 'descripcion': 'Miles Morales descubre que no es el unico Spider-Man en el multiverso.', 'anio': 2018, 'genero': 'Animacion', 'imagen': 'https://upload.wikimedia.org/wikipedia/en/f/fa/Spider-Man_Into_the_Spider-Verse_poster.png', 'video_url': 'https://www.youtube.com/watch?v=k-8ZFn1Askc'},
    {'titulo': 'Soul', 'descripcion': 'Un profesor de jazz viaja a un reino espiritual para encontrar su proposito.', 'anio': 2020, 'genero': 'Animacion', 'imagen': 'https://upload.wikimedia.org/wikipedia/en/3/39/Soul_%282020_film%29_poster.jpg', 'video_url': 'https://www.youtube.com/watch?v=hBUDtda8g8Q'},
    {'titulo': 'Encanto', 'descripcion': 'La unica sin magia en una familia magica descubre su verdadero don.', 'anio': 2021, 'genero': 'Animacion', 'imagen': 'https://upload.wikimedia.org/wikipedia/en/8/83/Encanto_poster.jpg', 'video_url': 'https://www.youtube.com/watch?v=SAH_W9q_brE'},
    # Terror
    {'titulo': 'The Babadook', 'descripcion': 'Una madre viuda lucha contra una criatura sobrenatural que aparece en un libro.', 'anio': 2014, 'genero': 'Terror', 'imagen': 'https://upload.wikimedia.org/wikipedia/en/d/d7/The-Babadook-Poster.jpg', 'video_url': 'https://www.youtube.com/watch?v=k5WQZzDRVtw'},
    {'titulo': 'Get Out', 'descripcion': 'Un joven negro descubre secretos perturbadores en la familia de su novia blanca.', 'anio': 2017, 'genero': 'Terror', 'imagen': 'https://upload.wikimedia.org/wikipedia/en/a/a3/Get_Out_poster.png', 'video_url': 'https://www.youtube.com/watch?v=hzTZKeSqOeg'},
    {'titulo': 'Hereditary', 'descripcion': 'Una familia enfrenta un oscuro legado tras la muerte de la abuela.', 'anio': 2018, 'genero': 'Terror', 'imagen': 'https://upload.wikimedia.org/wikipedia/en/d/d9/Hereditary.png', 'video_url': 'https://www.youtube.com/watch?v=V6wWKNij_1M'},
    {'titulo': 'A Quiet Place', 'descripcion': 'Una familia debe vivir en silencio para evitar a criaturas que cazan por sonido.', 'anio': 2018, 'genero': 'Terror', 'imagen': 'https://upload.wikimedia.org/wikipedia/en/a/a0/A_Quiet_Place_film_poster.png', 'video_url': 'https://www.youtube.com/watch?v=MxSIK-jngVA'},
    # Romance
    {'titulo': 'The Fault in Our Stars', 'descripcion': 'Dos adolescentes con cancer se enamoran y viven una historia inolvidable.', 'anio': 2014, 'genero': 'Romance', 'imagen': 'https://upload.wikimedia.org/wikipedia/en/4/41/The_Fault_in_Our_Stars_%28Official_Film_Poster%29.png', 'video_url': 'https://www.youtube.com/watch?v=9Lt8QAZkc94'},
    {'titulo': 'La La Land', 'descripcion': 'Un musico y una actriz persiguen sus suenos en Los Angeles mientras se enamoran.', 'anio': 2016, 'genero': 'Romance', 'imagen': 'https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png', 'video_url': 'https://www.youtube.com/watch?v=VDMf9m7FXd4'},
    {'titulo': 'Call Me by Your Name', 'descripcion': 'Un joven descubre el amor y el deseo durante un verano en Italia.', 'anio': 2017, 'genero': 'Romance', 'imagen': 'https://upload.wikimedia.org/wikipedia/en/c/c9/CallMeByYourName2017.png', 'video_url': 'https://www.youtube.com/watch?v=CDR8oapp2Wo'},
    {'titulo': 'Past Lives', 'descripcion': 'Dos amigos de la infancia se reencuentran decadas despues y reflexionan sobre sus vidas.', 'anio': 2023, 'genero': 'Romance', 'imagen': 'https://upload.wikimedia.org/wikipedia/en/d/da/Past_Lives_film_poster.png', 'video_url': 'https://www.youtube.com/watch?v=tINUmaEN-8M'},
]

class Command(BaseCommand):
    help = 'Limpia y puebla la BD con peliculas de 2014-2026'

    def add_arguments(self, parser):
        parser.add_argument('--if-empty', action='store_true', help='Solo poblar si no hay peliculas')

    def handle(self, *args, **options):
        if options['if_empty'] and Pelicula.objects.exists():
            self.stdout.write('Ya hay peliculas, saltando seed')
            return
        self.stdout.write('Limpiando base de datos...')
        Pelicula.objects.all().delete()
        Genero.objects.all().delete()
        self.stdout.write('OK - Base de datos limpia')
        generos = {}
        for p in PELICULAS:
            g, _ = Genero.objects.get_or_create(nombre=p['genero'])
            generos[p['genero']] = g
        for p in PELICULAS:
            Pelicula.objects.create(
                titulo=p['titulo'],
                descripcion=p['descripcion'],
                anio=p['anio'],
                genero=generos[p['genero']],
                imagen=p['imagen'],
                video_url=p['video_url'],
            )
            self.stdout.write(self.style.SUCCESS(f'  + {p["titulo"]} ({p["anio"]})'))
        self.stdout.write(self.style.SUCCESS(f'\nOK - {len(PELICULAS)} peliculas cargadas'))
