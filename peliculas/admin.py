from django.contrib import admin
from .models import Genero, Pelicula, Favorito, HistorialVisualizacion

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'anio', 'genero')


@admin.register(Favorito)
class FavoritoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'pelicula', 'creado')


@admin.register(HistorialVisualizacion)
class HistorialVisualizacionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'pelicula', 'visto_en')
