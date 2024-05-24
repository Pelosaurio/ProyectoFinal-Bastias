from django.shortcuts import redirect, render
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

def registrar_usuario(request):
    if request.method == "POST":
        form = forms.RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Comunidad:home")
    else: 
        form = forms.RegistrarUsuarioForm()
    return render(request, "Comunidad/registrar_usuario.html", context={"form": form})