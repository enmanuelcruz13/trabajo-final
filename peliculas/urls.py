from django.urls import path
from . import views

app_name = 'peliculas'

urlpatterns = [
    path('', views.index, name='index'),
    path('pelicula/<int:pk>/', views.detalle, name='detalle'),
    path('pelicula/<int:pk>/favorito/', views.toggle_favorito, name='toggle_favorito'),
    path('pelicula/<int:pk>/calificar/', views.calificar_pelicula, name='calificar_pelicula'),
    path('favoritos/', views.mis_favoritos, name='mis_favoritos'),
    path('agregar/', views.agregar_pelicula, name='agregar_pelicula'),
]
