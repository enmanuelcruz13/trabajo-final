from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Genero(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    anio = models.IntegerField(null=True, blank=True)
    imagen = models.URLField(blank=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'pelicula')
