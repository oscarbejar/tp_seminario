from Mensajes import *
from MenuPpl import *

def ingresarOpcion():
    msj = "Ingrese por favor opcion: "
    opcion = input(msj)
    res = validar(opcion,msj)
    return res

def validar(option, msj):
    msjnovalida = "\n********¡Opción no valida!***********\n" 
    while not option.isdigit() or (int(option) not in menuPpl().keys()):
        mostrarMenuPpl()
        print(msjnovalida)
        option = input(msj)
    return option
    
    