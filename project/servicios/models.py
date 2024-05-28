from django.db import models

class Servicios(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.CharField(max_length=500, verbose_name="descripción")
    valor = models.IntegerField(verbose_name="valor (CLP)")
    cantidad = models.IntegerField(null=True, blank=True)
        
    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name = "Nuestros Servicios"
        verbose_name_plural = "Nuestros Servicios"
