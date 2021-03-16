from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar_perfil/', views.agregar_perfil, name='agregar_perfil'),
    path('reportes/', views.ver_reportes, name='reporte'),
    path('reportes/pdf/<int:id>/', views.generar_reporte, name='generar_reporte')
]