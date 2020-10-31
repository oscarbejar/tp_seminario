from Mensajes import *
from MenuPpl import *
from Validador import *
from Inventario import *


def main():
    bienvenida()
    mostrarMenuPpl()
    op = ingresarOpcion("Seleccione por favor opcion: ")
    op =validarMenu(op,"Seleccione por favor opcion: ")
    msjSeleccionarOpcion(op)
    seleccion(op)


    #despedida()
main()