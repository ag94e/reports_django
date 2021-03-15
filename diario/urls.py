from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar_perfil/', views.agregar_perfil, name="agregar_perfil"),
]