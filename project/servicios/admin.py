from django.contrib import admin

from . import models

admin.site.site_title = "Servicios"

class ServiciosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "valor", "cantidad")
    list_display_links = ("nombre",)

admin.site.register(models.Servicios, ServiciosAdmin)
