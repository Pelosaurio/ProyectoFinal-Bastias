from django.shortcuts import redirect, render
from . import forms, models

def home(request):
    query = models.Comunidad.objects.all()
    context = {"comunidades": query}
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