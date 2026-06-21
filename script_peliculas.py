#!/usr/bin/env python
"""
Script para agregar peliculas a la BD (2014-2026).
Uso: python manage.py shell < script_peliculas.py
"""
from peliculas.models import Pelicula, Genero

generos = {}
for nombre in ['Accion', 'Drama', 'Comedia', 'Ciencia Ficcion', 'Animacion', 'Terror', 'Romance']:
    generos[nombre] = Genero.objects.get_or_create(nombre=nombre)[0]

peliculas = [
    ('Accion', 'Mad Max: Fury Road', 'En un futuro distopico, Max se une a una rebelion para cruzar el desierto.', 2015, 'https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg', 'https://www.youtube.com/watch?v=hEJnMQG9ev8'),
    ('Accion', 'John Wick', 'Un exasesino sale del retiro para vengar la muerte de su perro.', 2014, 'https://upload.wikimedia.org/wikipedia/en/9/98/John_Wick_TeaserPoster.jpg', 'https://www.youtube.com/watch?v=R7EJx1o0dCk'),
    ('Accion', 'Mission: Impossible - Fallout', 'Ethan Hunt debe detener una amenaza nuclear.', 2018, 'https://upload.wikimedia.org/wikipedia/en/f/ff/MI_%E2%80%93_Fallout.jpg', 'https://www.youtube.com/watch?v=wb49-oV0F78'),
    ('Accion', 'The Equalizer', 'Un hombre con un pasado letal ayuda a una joven.', 2014, 'https://upload.wikimedia.org/wikipedia/en/8/81/The_Equalizer_poster.jpg', 'https://www.youtube.com/watch?v=Uo9m5m3t5Hk'),
    ('Drama', 'Whiplash', 'Un joven baterista lucha por la perfeccion.', 2014, 'https://upload.wikimedia.org/wikipedia/en/0/01/Whiplash_poster.jpg', 'https://www.youtube.com/watch?v=7d_jQycdQGo'),
    ('Drama', 'The Revenant', 'Un trampero lucha por sobrevivir.', 2015, 'https://upload.wikimedia.org/wikipedia/en/b/b6/The_Revenant_2015_film_poster.jpg', 'https://www.youtube.com/watch?v=LoebZZ8K5N0'),
    ('Drama', 'Moonlight', 'La vida de un joven negro gay en Miami.', 2016, 'https://upload.wikimedia.org/wikipedia/en/8/84/Moonlight_%282016_film%29.png', 'https://www.youtube.com/watch?v=9NJj12tJzqc'),
    ('Drama', 'Parasite', 'Una familia pobre se infiltra en la vida de una familia rica.', 2019, 'https://upload.wikimedia.org/wikipedia/en/5/53/Parasite_%282019_film%29.png', 'https://www.youtube.com/watch?v=5xH0HfJHsaY'),
    ('Drama', 'Oppenheimer', 'La historia del fisico que creo la bomba atomica.', 2023, 'https://upload.wikimedia.org/wikipedia/en/4/4a/Oppenheimer_%28film%29.jpg', 'https://www.youtube.com/watch?v=uYPbbksJxIg'),
    ('Comedia', 'The Grand Budapest Hotel', 'Aventuras de un conserje en un hotel europeo.', 2014, 'https://upload.wikimedia.org/wikipedia/en/1/1c/The_Grand_Budapest_Hotel.png', 'https://www.youtube.com/watch?v=1Fg5iWmQjwk'),
    ('Comedia', 'Deadpool', 'Un mercenario con humor retorcido busca venganza.', 2016, 'https://upload.wikimedia.org/wikipedia/en/2/23/Deadpool_%282016_poster%29.png', 'https://www.youtube.com/watch?v=X5l8yFqX1N4'),
    ('Comedia', 'Everything Everywhere All at Once', 'Una migrante accede a realidades paralelas.', 2022, 'https://upload.wikimedia.org/wikipedia/en/1/1e/Everything_Everywhere_All_at_Once.jpg', 'https://www.youtube.com/watch?v=wxN1T1uxQ2g'),
    ('Comedia', 'Barbie', 'Barbie y Ken viajan al mundo real.', 2023, 'https://upload.wikimedia.org/wikipedia/en/0/0b/Barbie_2023_poster.jpg', 'https://www.youtube.com/watch?v=1RreqiMWCVQ'),
    ('Ciencia Ficcion', 'Interstellar', 'Astronautas viajan por un agujero de gusano.', 2014, 'https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg', 'https://www.youtube.com/watch?v=zSWdZVtXT7E'),
    ('Ciencia Ficcion', 'The Martian', 'Un astronauta varado en Marte.', 2015, 'https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg', 'https://www.youtube.com/watch?v=ej3ioOneTy8'),
    ('Ciencia Ficcion', 'Arrival', 'Una linguista se comunica con extraterrestres.', 2016, 'https://upload.wikimedia.org/wikipedia/en/d/df/Arrival%2C_Movie_Poster.jpg', 'https://www.youtube.com/watch?v=tFMo3UZNzqo'),
    ('Ciencia Ficcion', 'Dune', 'Un joven viaja a un planeta desertico.', 2021, 'https://upload.wikimedia.org/wikipedia/en/8/8e/Dune_%282021_film%29.jpg', 'https://www.youtube.com/watch?v=n9xhJsAgZmw'),
    ('Animacion', 'Inside Out', 'Las emociones de una nina trabajan juntas.', 2015, 'https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg', 'https://www.youtube.com/watch?v=yRUAzGQ3nSY'),
    ('Animacion', 'Coco', 'Un joven musico descubre el mundo de los muertos.', 2017, 'https://upload.wikimedia.org/wikipedia/en/9/98/Coco_%282017_film%29_poster.jpg', 'https://www.youtube.com/watch?v=Ga6RYdjcF9g'),
    ('Animacion', 'Spider-Man: Into the Spider-Verse', 'Miles Morales descubre el multiverso.', 2018, 'https://upload.wikimedia.org/wikipedia/en/f/fa/Spider-Man_Into_the_Spider-Verse_poster.png', 'https://www.youtube.com/watch?v=g4Hbz2jLx3E'),
    ('Animacion', 'Soul', 'Un profesor de jazz viaja a un reino espiritual.', 2020, 'https://upload.wikimedia.org/wikipedia/en/3/39/Soul_%282020_film%29_poster.jpg', 'https://www.youtube.com/watch?v=xOcT-EwECVo'),
    ('Animacion', 'Encanto', 'La unica sin magia en una familia magica.', 2021, 'https://upload.wikimedia.org/wikipedia/en/8/83/Encanto_poster.jpg', 'https://www.youtube.com/watch?v=CaimKeDcudo'),
    ('Terror', 'The Babadook', 'Una madre lucha contra una criatura sobrenatural.', 2014, 'https://upload.wikimedia.org/wikipedia/en/d/d7/The-Babadook-Poster.jpg', 'https://www.youtube.com/watch?v=k5WQZz9oX7A'),
    ('Terror', 'Get Out', 'Un joven descubre secretos en la familia de su novia.', 2017, 'https://upload.wikimedia.org/wikipedia/en/a/a3/Get_Out_poster.png', 'https://www.youtube.com/watch?v=DzfpyUB60YY'),
    ('Terror', 'Hereditary', 'Una familia enfrenta un oscuro legado.', 2018, 'https://upload.wikimedia.org/wikipedia/en/d/d9/Hereditary.png', 'https://www.youtube.com/watch?v=V6wWKNij_1M'),
    ('Terror', 'A Quiet Place', 'Una familia debe vivir en silencio.', 2018, 'https://upload.wikimedia.org/wikipedia/en/a/a0/A_Quiet_Place_film_poster.png', 'https://www.youtube.com/watch?v=WR7cc5t7tv8'),
    ('Romance', 'The Fault in Our Stars', 'Dos adolescentes con cancer se enamoran.', 2014, 'https://upload.wikimedia.org/wikipedia/en/4/41/The_Fault_in_Our_Stars_%28Official_Film_Poster%29.png', 'https://www.youtube.com/watch?v=9ItBvH5J6Ss'),
    ('Romance', 'La La Land', 'Un musico y una actriz persiguen sus suenos.', 2016, 'https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png', 'https://www.youtube.com/watch?v=0pdqf4P9MB8'),
    ('Romance', 'Call Me by Your Name', 'Un joven descubre el amor en Italia.', 2017, 'https://upload.wikimedia.org/wikipedia/en/c/c9/CallMeByYourName2017.png', 'https://www.youtube.com/watch?v=Z9AYPxH5NTM'),
    ('Romance', 'Past Lives', 'Dos amigos se reencuentran decadas despues.', 2023, 'https://upload.wikimedia.org/wikipedia/en/d/da/Past_Lives_film_poster.png', 'https://www.youtube.com/watch?v=kA2qg1ZpAkc'),
]

for genero_nombre, titulo, desc, anio, img, vid in peliculas:
    Pelicula.objects.get_or_create(
        titulo=titulo,
        defaults={
            'descripcion': desc,
            'anio': anio,
            'genero': generos[genero_nombre],
            'imagen': img,
            'video_url': vid,
        }
    )
    print(f'  + {titulo} ({anio})')

print(f'\nOK - {len(peliculas)} peliculas cargadas')
print(f'Total en BD: {Pelicula.objects.count()}')
