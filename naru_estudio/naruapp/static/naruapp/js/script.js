window.onload = function() {

    // FUNCIONES
    function LinkeaExplorar() {
        window.location.href = "/naru-estudio/entradas";
    };

    function OcultarPilar () {
        pilar.classList.toggle("hidden");
    }

    // MANEJADOR DE EVENTOS
    const divExplorar = document.querySelector(".divExplorar")
    const divHamburguesa = document.querySelector(".divHamburguesa")
    const pilar = document.querySelector(".sidebar")

    divExplorar.addEventListener("click", LinkeaExplorar)
    divHamburguesa.addEventListener("click", OcultarPilar)

}