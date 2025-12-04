from django.urls import path
from . import views

urlpatterns = [
    path('', views.cuenta_ingreso, name="cuenta_ingreso"),
    path('registro/', views.cuenta_registro, name="cuenta_registro"),
    path('registro-exitoso/', views.cuenta_registro_ok, name="cuenta_registro_ok"),
    path('clases/', views.naru_clases),
    path('entradas/', views.naru_entradas, name='naru_entradas'),
    path('entradas/<int:id>', views.naru_entrada, name="naru_entrada"),
    path('entradas/crear-entrada', views.naru_entrada_nueva, name="naru_entrada_nueva")
]