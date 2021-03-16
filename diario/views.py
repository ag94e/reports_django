from django.shortcuts import render, redirect
from .forms import PerfilForm, DiarioForm
from .models import Perfil, Diario, DiarioPorFecha

from datetime import date

def inicio(request):
    diario = DiarioForm()
    form = PerfilForm()
    today = date.today()
    if request.method == 'GET':
        today = date.today().strftime('%d/%m/%Y')
        gerentes = Perfil.objects.filter(es_gerente=True)
        context = {
            'today': today,
            'diario': diario,
            'form': form,
            'gerentes': gerentes,
        }
        return render(request, 'home.html', context)

    elif request.method == 'POST':
        diario = DiarioForm(request.POST)
        if diario.is_valid():
            condicion = Diario.objects.filter(brm=diario.cleaned_data['brm'], fecha=today)
            if condicion.count() == 1:
                cond = Diario.objects.get(brm=diario.cleaned_data['brm'], fecha=today)
                today = date.today().strftime('%d/%m/%Y')
                gerentes = Perfil.objects.filter(es_gerente=True)
                context = {
                    'today': today,
                    'diario': diario,
                    'form': form,
                    'gerentes': gerentes,
                    'message_1': f'Ya esta capturado el día de hoy {cond.brm}'
                }
                return render(request, 'home.html', context)
            else:
                guardar_diaro = Diario.objects.create(**diario.cleaned_data)
                agregar_diario = Diario.objects.get(brm=diario.cleaned_data['brm'], fecha=today)
                gerente_en_turno = Perfil.objects.get(brm=request.POST['gerente'])
                try:
                    reporte = DiarioPorFecha.objects.get(fecha=today)
                    today = date.today().strftime('%d/%m/%Y')
                    gerentes = Perfil.objects.filter(es_gerente=True)
                    context = {
                        'today': today,
                        'diario': diario,
                        'form': form,
                        'gerentes': gerentes,
                        'message_2': f'Se agregó {agregar_diario.brm.nombre} al reporte de hoy'
                    }
                    return render(request, 'home.html', context)

                except DiarioPorFecha.DoesNotExist:
                    reporte = DiarioPorFecha.objects.create(gerente_turno=gerente_en_turno)
                    return render(request, 'home.html')
                



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
            form.save()
            return redirect('inicio')

    return render(request, 'agregar_perfil.html')

def ver_reportes(request):
    return render(request, 'reporte.html')
