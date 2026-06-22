from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:profile')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    user = request.user
    total_favoritos = user.favorito_set.count()
    total_calificaciones = user.calificacion_set.count()
    return render(request, 'registration/profile.html', {
        'profile': user.profile,
        'total_favoritos': total_favoritos,
        'total_calificaciones': total_calificaciones,
    })


@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        avatar = request.POST.get('avatar', '').strip()
        if avatar:
            profile.avatar = avatar
            profile.save()
            messages.success(request, 'Perfil actualizado correctamente.')
        else:
            messages.error(request, 'Debes ingresar una URL de imagen.')
        return redirect('accounts:profile')
    return render(request, 'registration/edit_profile.html', {'profile': profile})
