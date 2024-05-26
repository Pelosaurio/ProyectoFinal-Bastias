from django.shortcuts import redirect, render
from . import models, forms

def home(request):
    consulta_servicios = models.ServiciosCategoria.objects.all()
    context = {"servicios": consulta_servicios}
    return render(request, "servicios/index.html", context)

def servicios_detalle(request, pk: int):
    query = models.ServiciosCategoria.objects.get(id=pk)
    return render(request, "servicios/detalleservicio.html", {"servicio": query})

def servicios_crear(request):
    if request.method == "POST":
        form = forms.CrearServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("servicios:home")
    else:
        form = forms.CrearServicioForm()
    return render(request, "servicios/crearservicio.html", context={"form":form})

def servicios_actualizar(request, pk: int):
    query = models.ServiciosCategoria.objects.get(id=pk)
    if request.method == "POST":
        form = forms.CrearServicioForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("servicios:home")
    else:
        form = forms.CrearServicioForm(instance=query)
    return render(request, "servicios/actualizarservicio.html", context={"form":form})

def servicios_borrar(request, pk: int):
    query = models.ServiciosCategoria.objects.get(id=pk)
    if request.method == "POST":
        query.delete()
        return redirect("servicios:home")
    return render(request, "servicios/borrarservicio.html", context={"servicio":query})