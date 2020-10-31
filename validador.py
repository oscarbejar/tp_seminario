from menuPpl import *

def validar(option, msj):
    msjnovalida = "Opción no valida" 
    while not option.isdigit():
        print(msjnovalida)
        option = input(msj)
    while int(option) not in menuPpl().keys():
        print(msjnovalida)
        option = int(input(msj))
    return option
    
    