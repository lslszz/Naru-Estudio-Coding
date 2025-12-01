from django.contrib import admin
from django.db import models
from django.shortcuts import redirect
from .models import Usuario


# --------------------------------------------------------------
# REGISTRO DE MODELS
# --------------------------------------------------------------

admin.site.register(Usuario)

# --------------------------------------------------------------
# REGISTRO DE VIEWS
# --------------------------------------------------------------

modelsViews = []

class AdminViewModel_CuentaRegistro(models.Model):
    url = '/naru-estudio/registro'
    class Meta:
        verbose_name = "View Registro"
        verbose_name_plural = "View Registro"
        managed = False

modelsViews.append(AdminViewModel_CuentaRegistro)

def Registrar_Views():
    for model in modelsViews:
        class AdminLink(admin.ModelAdmin):
            url = model.url
            def changelist_view(self, request, extra_context=None):
                # Redirige al template real de productos
                return redirect(self.url)  # URL que ya funciona
        admin.site.register(model, AdminLink)

Registrar_Views()

