from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models, forms

def home(request):
    consulta_servicios = models.ServiciosCategoria.objects.all()
    context = {"servicios": consulta_servicios}
    return render(request, "servicios/index.html", context)

def servicios_detalle(request, pk: int):
    query = models.ServiciosCategoria.objects.get(id=pk)
    return render(request, "servicios/detalleservicio.html", {"servicio": query})

class ServicioCrear(LoginRequiredMixin, CreateView):
    model = models.ServiciosCategoria
    template_name = "servicios/crearservicio.html"
    form_class = forms.CrearServicioForm
    success_url = reverse_lazy("servicios:home")
    
class ServicioActualizar(LoginRequiredMixin, UpdateView):
    model = models.ServiciosCategoria
    template_name = "servicios/actualizarservicio.html"
    form_class = forms.CrearServicioForm
    success_url = reverse_lazy("servicios:home")

class ServicioBorrar(LoginRequiredMixin, DeleteView):
    model = models.ServiciosCategoria
    template_name = "servicios/borrarservicio.html"
    success_url = reverse_lazy("servicios:home")


