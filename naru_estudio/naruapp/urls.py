from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home_app, name='home_app'),
    path('registro/', views.cuenta_registro, name='cuenta_registro'),
    #path('crear/', views.crear_producto, name='crear_producto'),
    #path('leer/<int:id>', views.leer_producto, name='leer_producto'),
    #path('leer-todos', views.leer_todos, name='leer_todos'),
    #path('actualizar/<int:id>', views.actualizar_producto, name='actualizar_producto'),
    #path('eliminar/<int:id>', views.eliminar_producto, name='eliminar_producto'),
]