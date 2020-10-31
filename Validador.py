from Mensajes import *
from MenuPpl import *

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