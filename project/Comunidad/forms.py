from django import forms
from . import models

class RegistrarUsuarioForm(forms.ModelForm):
    class Meta:
        model = models.Usuario 
        fields = '__all__'
