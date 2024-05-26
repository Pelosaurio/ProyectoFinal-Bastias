from django.db import models

class ServiciosCategoria(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.CharField(max_length=300, verbose_name="descripción")
        
    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name = "Nuestros Servicios"
        verbose_name_plural = "Nuestros Servicios"
