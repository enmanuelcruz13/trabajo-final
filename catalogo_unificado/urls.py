from django.contrib import admin
from django.urls import path, include
from .views import healthz

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('peliculas.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('healthz', healthz),
]
