from django.urls import path
from . import views

app_name = "servicios"

urlpatterns = [
    path('', views.home, name="home"),
    path('crearservicio/', views.servicios_crear, name="servicios_crear"),
    path('detalleservicio/<int:pk>', views.servicios_detalle, name="servicios_detalle"),
    path('actualizarservicio/<int:pk>', views.servicios_actualizar, name="servicios_actualizar"),
    path('borrarservicio/<int:pk>', views.servicios_borrar, name="servicios_borrar")
    ]