from Inventario import *
from Validador import *

def modificacion():
    return None

def modificarArt():
    msjnovalida = "********¡Tipo de Dato no valido!***********\n" 

    msjID = "Ingresar ID del Articulo a Modificar : "
    idArt = confirmacion(msjID)
    while not idArt.isdigit():
        print(msjnovalida)
        idArt = confirmacion(msjID)

    while int(idArt) not in articulos.keys():
        print("*****ID ingresado no existe*****")
        idArt = confirmacion(msjID)

    print("Seleccione el campo a modificar : ")
    
    for i in articulos[0].keys():
        print(i)
