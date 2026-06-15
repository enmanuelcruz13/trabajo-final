from django.contrib import admin
from .models import Genero, Pelicula, Favorito, Calificacion

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'anio', 'genero')

@admin.register(Favorito)
class FavoritoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'pelicula', 'creado')

@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'pelicula', 'puntuacion', 'creado')
