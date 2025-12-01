from django.shortcuts import render, redirect
from .forms import UsuarioForm

# Views de la aplicación (FBV)

def cuenta_registro(request):
    # Envío de formulario
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("registro_ok")

    # Primera carga de la página
    else:
        form = UsuarioForm()

    return render(request, "naruapp/registro.html", {"form": form})