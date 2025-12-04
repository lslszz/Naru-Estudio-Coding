window.onload = function() {

    // FUNCIONES
    function LinkeaExplorar() {
        window.location.href = "/naru-estudio/entradas";
    };


    // MANEJADOR DE EVENTOS
    divExplorar = document.querySelector(".divExplorar")

    divExplorar.addEventListener("click", LinkeaExplorar)



}