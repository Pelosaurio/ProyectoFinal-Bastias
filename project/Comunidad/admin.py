from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Psicologa)
admin.site.register(models.Equipo)
admin.site.register(models.Usuario)
admin.site.register(models.Comunidad)