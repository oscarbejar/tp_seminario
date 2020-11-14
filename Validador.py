from Mensajes import *
from MenuPpl import *
from Inventario import *

def ingresarOpcion(msj):
    opcion = input(msj)
    res = validarN(opcion, msj)
    return res

def validarN(option, msj):
    msjnovalida = "********¡Tipo de Dato no valido!***********" 
    while not option.isdigit():
        print(msjnovalida)
        option = input(msj)
    return option
    
def validarMenu(option, msj, menu):
    msjnovalida = "\n********¡Opción no encontrada!***********\n" 
    while not option.isdigit() or (int(option) not in menu.keys()):
        mostrarMenuPpl()
        print(msjnovalida)
        option = input(msj)
    return option  




   

def confirmacion(msj):
    print("")
    op = input(msj)
    print("\n Ingresaste: ", op)
    conf = input("¿Es Correcto? (Y/n): ")
    while (conf != "y" and conf != "Y" and conf != ""):
        op = input(msj)
        print("\nIngresaste: ", op)
        conf = input("Es Correcto? (Y/n): ")
    return op






def repetirOperacion():
    print("")
    conf = input("¿Deseas realizar otra operación? (y/N): ")
    return conf
    
