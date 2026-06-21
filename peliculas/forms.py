from django import forms
from .models import Pelicula


class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['titulo', 'descripcion', 'anio', 'imagen', 'video_url', 'genero']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título',
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Sinopsis o descripción...',
                'rows': 4,
            }),
            'anio': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 2024',
            }),
            'imagen': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://ejemplo.com/poster.jpg',
            }),
            'video_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://www.youtube.com/watch?v=...',
            }),
            'genero': forms.Select(attrs={
                'class': 'select-input',
            }),
        }
        labels = {
            'titulo': 'Título',
            'descripcion': 'Descripción',
            'anio': 'Año',
            'imagen': 'URL del Póster',
            'video_url': 'URL del Video/Trailer',
            'genero': 'Género',
        }
