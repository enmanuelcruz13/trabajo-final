from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('pelicula/<int:pk>/', views.detalle, name='detalle'),
    path('pelicula/<int:pk>/favorito/', views.agregar_favorito, name='agregar_favorito'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('accounts/register/', views.register, name='register'),
]
