from django.shortcuts import redirect, render
from . import models, forms

def home(request):
    consulta_servicios = models.ServiciosCategoria.objects.all()
    context = {"servicios": consulta_servicios}
    return render(request, "servicios/index.html", context)

def servicios_create(request):
    if request.method == "POST":
        form = forms.CrearServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("servicios:home")
    else:
        form = forms.CrearServicioForm
    return render(request, "servicios/crearservicio.html", context={"form":form})