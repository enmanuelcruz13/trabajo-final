from django.contrib import admin
from django.urls import path, include
from .views import healthz

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('peliculas.urls')),
    path('healthz', healthz),
]
