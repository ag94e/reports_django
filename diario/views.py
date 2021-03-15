from django.shortcuts import render
from .forms import PerfilForm
from .models import Perfil

from datetime import date

def inicio(request):
    today = date.today().strftime('%d/%m/%Y')
    # perfil = Perfil.objects.all()
    form = PerfilForm()
    context = {
        'today': today,
        # 'perfil': perfil,
        'form': form,
    }
    return render(request, 'home.html', context)

def agregar_perfil(request):
    form = PerfilForm()
    if request.method == "GET":
        context = {
            'form': form,
        }
        return render(request, 'agregar_perfil.html', context)
    elif request.method == 'POST':
        form = PerfilForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        context = {
            'form': form,
        }
        return render(request, 'agregar_perfil.html', context)
    return render(request, 'agregar_perfil.html')
