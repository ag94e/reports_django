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

# class DiarioForm(ModelForm):
#     pass


# class DiarioPorFechaForm(ModelForm):
#     pass