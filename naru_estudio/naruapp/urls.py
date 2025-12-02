from django.urls import path
from . import views

urlpatterns = [
    path('', views.cuenta_ingreso),
    path('registro/', views.cuenta_registro),
    path('registro-exitoso/', views.cuenta_registro_ok, name="cuenta_registro_ok"),
    path('clases/', views.naru_clases),
    path('entradas/', views.naru_entradas),
    path('entradas/<int:id>', views.naru_entrada, name="naru_entrada"),
    path('entradas/crear-entrada', views.naru_entrada_nueva, name="naru_entrada_nueva")
    #path('crear/', views.crear_producto, name='crear_producto'),
    #path('leer/<int:id>', views.leer_producto, name='leer_producto'),
    #path('leer-todos', views.leer_todos, name='leer_todos'),
    #path('actualizar/<int:id>', views.actualizar_producto, name='actualizar_producto'),
    #path('eliminar/<int:id>', views.eliminar_producto, name='eliminar_producto'),
]