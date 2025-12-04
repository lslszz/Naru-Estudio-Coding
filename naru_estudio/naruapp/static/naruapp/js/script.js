window.onload = function() {

    // FUNCIONES
    function LinkeaExplorar() {
        window.location.href = "/naru-estudio/entradas";
    };

    function LinkeaClases() {
        window.location.href = "/naru-estudio/clases";
    };

    function OcultarPilar () {
        pilar.classList.toggle("hidden");
    }

    // MANEJADOR DE EVENTOS
    const divExplorar = document.querySelector(".divExplorar")
    const divClases = document.querySelector(".divClases")
    const divHamburguesa = document.querySelector(".divHamburguesa")
    const pilar = document.querySelector(".sidebar")

    divExplorar.addEventListener("click", LinkeaExplorar)
    divClases.addEventListener("click", LinkeaClases)
    divHamburguesa.addEventListener("click", OcultarPilar)


}