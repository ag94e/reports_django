from django.shortcuts import render
from .forms import PerfilForm
from . models import Perfil

from datetime import date

def inicio(request):
    today = date.today().strftime('%d/%m/%Y')
    perfil = Perfil.objects.all()
    form = PerfilForm()
    context = {
        'today': today,
        'perfil': perfil,
        'form': form,
    }
    return render(request, 'inicio.html', context)
