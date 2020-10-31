from Mensajes import *
from MenuPpl import *
from Validador import *
from Inventario import *


def main():
    bienvenida()
    mostrarMenuPpl()
    op = ingresarOpcion()
    msjSeleccionarOpcion(op)
    seleccion(op)


    #despedida()
main()