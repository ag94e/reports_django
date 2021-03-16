from django import forms
from .models import Perfil, Diario, DiarioPorFecha

class PerfilForm(forms.ModelForm):
    es_gerente = forms.BooleanField(required=False, label='¿Es gerente?', initial=False)

    class Meta:
        model = Perfil
        fields = [
            'nombre',
            'brm',
            'telefono',
            'sucursal',
            'ciudad',
            'estado',
            'es_gerente',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'brm': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'BRM'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'sucursal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sucursal'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad'}),
            'estado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estado'}),
        }

class DiarioForm(forms.ModelForm):
    brm = forms.ModelChoiceField(queryset=Perfil.objects.all(), widget=forms.Select(attrs={'class':'form-control'}), label="Colaborador")
    tos = forms.BooleanField(required=False, label='¿Tos?', initial=False)
    cabeza = forms.BooleanField(required=False, label='Dolor de cabeza?', initial=False)
    garganta = forms.BooleanField(required=False, label='¿Dolor de garganta?', initial=False)
    resfriado = forms.BooleanField(required=False, label='¿Resfriado?', initial=False)
    malestar_general = forms.BooleanField(required=False, label='¿Malestar en general?', initial=False)
    respirar = forms.BooleanField(required=False, label='¿Dificultad para respirar?', initial=False)

    class Meta:
        model = Diario
        fields = [
            'brm',
            'temperatura',
            'tos',
            'cabeza',
            'garganta',
            'resfriado',
            'malestar_general',
            'respirar'
        ]
        widgets = {
            'temperatura': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Temperatura'}),
        }