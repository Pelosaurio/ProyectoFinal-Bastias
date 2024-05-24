from django.shortcuts import redirect, render
from . import models

def home(request):
    consulta_servicios = models.ServiciosCategoria.objects.all()
    context = {"servicios": consulta_servicios}
    return render(request, "servicios/index.html", context)