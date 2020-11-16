
"""Importamos los demas archivos .py donde encopntraremos datos y funciones adicionales"""
from Mensajes import *
from MenuPpl import *
from Validador import *
from Inventario import *
from Ingresos import *
from Modificacion import *
from Ventas import *


"""Metodo main es el metodo principal del programa"""
def main():
    bienvenida()
    mostrarMenuPpl()
    mostrarProg()

    """Repetidor del programa"""
    conf = repetirOperacion()
    while (conf == "y" or conf == "Y"):
        mostrarMenuPpl()
        mostrarProg()
        conf = repetirOperacion()
    print("\nGuardando información...\n")
    guardarInventario()
    despedida()



main()
