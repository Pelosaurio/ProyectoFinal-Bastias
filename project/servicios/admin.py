from django.contrib import admin

from . import models

admin.site.site_title = "Servicios"

class ServiciosCategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    list_display_links = ("nombre",)

admin.site.register(models.ServiciosCategoria, ServiciosCategoriaAdmin)
