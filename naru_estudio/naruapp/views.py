from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UsuarioForm
from .models import Usuario


# ----------------------------------------------------------------------------
# VIEWS FBV de la APLICACIÓN
# ----------------------------------------------------------------------------
def cuenta_registro(request):
    # Envío de formulario
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            datos = form.save()
            messages.success(request, f"¡Bienvenido, {datos.nombre}!")
            return redirect("cuenta_registro_ok")


    # Primera carga de la página
    else:
        form = UsuarioForm()

    return render(request, "naruapp/registro.html", {"form": form})

def cuenta_registro_ok(request):
    return render (request, "naruapp/registro_ok.html")


def cuenta_ingreso(request):
    return render(request, "naruapp/index.html")


def naru_clases(request):
    return render(request, "naruapp/naru_clases.html")

def naru_entradas(request):
    return render(request, "naruapp/naru_entradas.html")