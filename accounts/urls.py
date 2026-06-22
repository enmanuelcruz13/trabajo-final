from django.urls import path
from .views import register, profile, edit_profile

app_name = 'accounts'

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
]
