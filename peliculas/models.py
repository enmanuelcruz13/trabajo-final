from django.db import models
from django.contrib.auth import get_user_model
import re
import requests
from django.conf import settings

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
    video_url = models.URLField(blank=True, help_text='URL de YouTube o enlace directo a video')
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)

    def get_embed_url(self):
        if not self.video_url:
            return ''
        if 'youtube.com/embed/' in self.video_url:
            return self.video_url
        match = re.search(r'(?:youtube\.com/watch\?v=|youtu\.be/)([\w-]+)', self.video_url)
        if match:
            vid = match.group(1)
            return f'https://www.youtube.com/embed/{vid}'
        return ''

    def get_youtube_id(self):
        if not self.video_url:
            return None
        match = re.search(r'(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)([\w-]+)', self.video_url)
        if match:
            return match.group(1)
        return None

    def get_youtube_thumbnail(self, quality='hqdefault'):
        video_id = self.get_youtube_id()
        if video_id:
            return f'https://img.youtube.com/vi/{video_id}/{quality}.jpg'
        return None

    def get_youtube_meta(self):
        """Return dict with title, description, thumbnails using YouTube Data API."""
        video_id = self.get_youtube_id()
        if not video_id:
            return {}
        api_key = getattr(settings, 'YOUTUBE_API_KEY', None)
        if not api_key:
            return {}
        url = (
            f"https://www.googleapis.com/youtube/v3/videos"
            f"?part=snippet,contentDetails&id={video_id}&key={api_key}"
        )
        try:
            resp = requests.get(url, timeout=5)
            resp.raise_for_status()
            data = resp.json()
            if data.get('items'):
                return data['items'][0]
        except Exception:
            return {}
        return {}


    @property
    def has_trailer(self):
        return bool(self.video_url)

    def __str__(self):
        return self.titulo


class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'pelicula')


class Calificacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE, related_name='calificaciones')
    puntuacion = models.IntegerField()  # 1 to 5
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'pelicula')

    def __str__(self):
        return f"{self.usuario.username} - {self.pelicula.titulo} - {self.puntuacion}★"


class HistorialVisualizacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    visto_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-visto_en']
        unique_together = ('usuario', 'pelicula')

    def __str__(self):
        return f"{self.usuario.username} vio {self.pelicula.titulo}"



