from django.contrib import admin
from django.shortcuts import redirect
from django.db import models
from .models import Lista


modelsViews = []

class AdminModel_HomeProducto(models.Model):
    url = '/productos/'
    class Meta:
        verbose_name = "View Home Producto"
        verbose_name_plural = "View Home Producto"
        managed = False

class AdminModel_LeerProductos(models.Model):
    url = '/productos/leer-todos'
    class Meta:
        verbose_name = "View Leer Producto"
        verbose_name_plural = "View Leer Producto"
        managed = False

modelsViews.append(AdminModel_HomeProducto)
modelsViews.append(AdminModel_LeerProductos)


# REGISTRO DE VIEWS
def Registrar_Views():
    for model in modelsViews:
        class AdminLink(admin.ModelAdmin):
            url = model.url
            def changelist_view(self, request, extra_context=None):
                # Redirige al template real de productos
                return redirect(self.url)  # URL que ya funciona
        admin.site.register(model, AdminLink)

Registrar_Views()

admin.site.register(Lista)