from django.urls import path
from . import views

app_name = 'peliculas_new'

urlpatterns = [
    path('', views.index, name='index'),
    path('pelicula/<int:pk>/', views.detalle, name='detalle'),
]
