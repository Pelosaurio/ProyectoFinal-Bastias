from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError

from django.utils import timezone

class Vendedor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name="Vendedor")
    telefono = models.PositiveIntegerField()
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)
    
    def __str__(self):
        return self.usuario
    
    class Meta: 
        verbose_name_plural = "Vendedores"

class Venta(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.DO_NOTHING)
    servicio = models.ForeignKey("servicios.Servicios", on_delete=models.DO_NOTHING)
    cantidad = models.PositiveIntegerField()
    precio_total = models.PositiveIntegerField(editable=False)
    fecha_venta = models.DateTimeField(default=timezone.now, editable=False)
    
    class Meta:
        ordering = ("-fecha_venta",)
        verbose_name_plural = "Ventas"
        
    def clean(self):
        if self.cantidad > self.servicio.cantidad:
            raise ValidationError("Has superado la cantidad disponible ☹")
        
    def save(self, *args, **kwargs):
        self.precio_total = self.servicio.valor * self.cantidad
        