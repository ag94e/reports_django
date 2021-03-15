from django import forms
from .models import Perfil, Diario, DiarioPorFecha

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = [
            # 'nombre',
            'telefono',
            'sucursal',
            'ciudad',
            'estado',
            'es_gerente',
        ]
        labels ={
            'es_gerente': 'Gerente',
        }
        widgets = {
            # 'nombre': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'sucursal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sucursal'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad'}),
            'estado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estado'}),
            'es_gerente': forms.BooleanField(attrs={'class': 'form-control', 'placeholder': '¿Gerente?'}),
        }

# class DiarioForm(ModelForm):
#     pass


# class DiarioPorFechaForm(ModelForm):
#     pass