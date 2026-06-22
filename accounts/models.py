from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.URLField(blank=True, help_text='URL de la imagen de perfil')

    def __str__(self):
        return f'Perfil de {self.user.username}'

    def get_avatar(self):
        if self.avatar:
            return self.avatar
        return f'https://ui-avatars.com/api/?name={self.user.username}&background=3b82f6&color=fff&size=128'
