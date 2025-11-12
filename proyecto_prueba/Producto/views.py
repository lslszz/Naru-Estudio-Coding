from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from urllib import request
from .models import Lista

# FBV home_producto
def home_producto(request):
    productos = Lista.objects.all()
    contexto = {
    'titulo': 'Bienvenido a Productos',
    'descripcion': 'Aquí verás una lista de productos ficticios.',
    'productos': productos
    }
    return render(request, 'Producto/vista.html', contexto)

# FBV crear_producto
def crear_producto(request):
    return render(request, 'Producto/crear.html')

# FBV leer_todos
def leer_todos(request):
    productos = Lista.objects.all()
    contexto = {
        "productos": productos
    }
    return render(request, "Producto/leer_todos.html", contexto)

# FBV leer_producto
def leer_producto(request, id):
    producto = get_object_or_404(Lista, id=id)
    context = {'producto': producto}
    return render(request, 'Producto/leer_producto.html', context)


# FBV actualizar_producto
def actualizar_producto(request, id):
    producto = get_object_or_404(Lista, id=id)
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.cantidad = request.POST.get('cantidad')
        producto.save()
        return leer_producto(request, id)
    else:
        context = {'producto': producto}
        return render(request, 'Producto/actualizar.html', context)


# FBV eliminar_producto
def eliminar_producto(request, id):
    producto = get_object_or_404(Lista, id=id)
    producto.delete()
    return leer_todos(request)

