from django import forms
from .models.Vehiculo import *

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = [
            'modelo',
            'color',
            'marca',
            'kilometraje',
            'nuevo'
        ]