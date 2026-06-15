from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pelicula/<int:pk>/', views.detalle, name='detalle'),
    path('pelicula/<int:pk>/favorito/', views.agregar_favorito, name='agregar_favorito'),
]
