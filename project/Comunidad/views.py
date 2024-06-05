from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from . import forms, models

def home(request):
    psicologas = models.Psicologa.objects.all()
    equipo = models.Equipo.objects.all()
    usuarios = models.Usuario.objects.all()
    context = {
        "psicologas": psicologas,
        "equipo": equipo, 
        "usuarios": usuarios
    }
    return render(request, "Comunidad/index.html", context)

class RegistrarUsuario(CreateView):
    model = models.Usuario
    template_name = "comunidad/registrarusuario.html"
    form_class = forms.RegistrarUsuarioForm
    success_url = reverse_lazy("Comunidad:home")
