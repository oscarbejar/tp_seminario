from Mensajes import *
from MenuPpl import *
from Validador import *
from Inventario import *
from Ingresos import *
from Modificacion import *
from Ventas import *

def main():
    bienvenida()
    mostrarMenuPpl()
    mostrarProg()


    conf = repetirOperacion()
    while (conf == "y" or conf == "Y"):
        mostrarMenuPpl()
        mostrarProg()
        conf = repetirOperacion()
    print("Stock Actual")
    verStock()
    print("\nGuardando información...\n")
    guardarInventario()
    despedida()



main()
