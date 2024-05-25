from django import forms
from . import models

class CrearServicioForm(forms.ModelForm):
    class Meta:
        model = models.ServiciosCategoria 
        fields = '__all__'
