from django.contrib import admin

from . import models

class VentaAdmin(admin.ModelAdmin):
    list_display = (
        "vendedor",
        "servicio",
        "cantidad",
        "precio_total",
        "descripcion",
        "fecha_venta",
    )
    list_display_links = ("servicio",)
    search_fields = ("servicio.nombre", "vendedor")
    list_filter = ("vendedor",)
    date_hierarchy = "fecha_venta"

admin.site.register(models.Vendedor)
admin.site.register(models.Venta, VentaAdmin)


