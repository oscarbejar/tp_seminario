from Mensajes import *
from MenuPpl import *
from Inventario import *

def ingresarOpcion(msj):
    opcion = input(msj)
    res = validarN(opcion, msj)
    return res

def validarN(option, msj):
    msjnovalida = "\n********¡Opción no valida!***********\n" 
    while not option.isdigit():
        print(msjnovalida)
        option = input(msj)
    return option
    
def validarMenu(option, msj):
    msjnovalida = "\n********¡Opción no valida!***********\n" 
    while not option.isdigit() or (int(option) not in menuPpl().keys()):
        mostrarMenuPpl()
        print(msjnovalida)
        option = input(msj)
    return option  

def validarVenta(option,msj):
    while not option.isdigit() or option not in articulos().keys():
        print("ingrese un id valido")
        option=input(msj)

    return option
def validarCantidad(option,msj, id):
    while option>articulos()[id]["Cantidad"]:
        print("la cantidad supera al stock disponible")
        option=input(msj)

    return option