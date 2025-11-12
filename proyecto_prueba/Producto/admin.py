from django.contrib import admin
from django.shortcuts import redirect
from django.db import models

# Modelo ficticio (solo para que aparezca el bloque en el admin)
class ProductoFicticio(models.Model):
    class Meta:
        verbose_name = "Productos"
        verbose_name_plural = "Productos"
        managed = False  # No crea ninguna tabla en la base de datos

# Clase del admin: solo redirige al hacer clic
class ProductoAdminLink(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        # Redirige al template real de productos
        return redirect('/productos/')  # URL que ya funciona

# Registrar el modelo en el admin
admin.site.register(ProductoFicticio, ProductoAdminLink)
