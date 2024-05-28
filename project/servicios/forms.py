from django import forms
from . import models

class CrearServicioForm(forms.ModelForm):
    class Meta:
        model = models.Servicios
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'background-color: #faf3e0; color: #000;',
                'maxlength': '200',
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'background-color: #faf3e0; color: #000;',
                'rows': 10,
                'maxlength': '500',
            }),
            'valor': forms.NumberInput(attrs={
                'class': 'form-control',
                'style': 'background-color: #faf3e0; color: #000;',
            }),
            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control',
                'style': 'background-color: #faf3e0; color: #000;',
            }),
        }