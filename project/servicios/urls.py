from django.urls import path
from . import views

app_name = "servicios"

urlpatterns = [
    path('', views.home, name="home"),
    path('crearservicio/', views.ServicioCrear.as_view(), name="servicios_crear"),
    path('detalleservicio/<int:pk>', views.servicios_detalle, name="servicios_detalle"),
    path('actualizarservicio/<int:pk>', views.ServicioActualizar.as_view(), name="servicios_actualizar"),
    path('borrarservicio/<int:pk>', views.ServicioBorrar.as_view(), name="servicios_borrar")
    ]