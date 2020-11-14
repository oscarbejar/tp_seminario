from Inventario import *
from Validador import *

def modificacion():
    return None

def valorN(op):
    while int(op) not in articulos[0].keys():
        print("Opcion no encontrada")
        op = int(ingresarOpcion("Seleccione el campo a modificar : "))
    return op

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


    j = 1
    for i in articulos[0].keys():
        print("\n{} - {}\n".format(j, i.upper()))
        j += 1

    opMod = int(ingresarOpcion("Seleccione el campo a modificar : "))


        
    if opMod == 1:
        msjMarca = "Ingrese Marca del Articulo: "
        marca = confirmacion(msjMarca)
        articulos[int(idArt)]["marca"] = marca
    elif opMod == 2:
        msjModelo = "Ingrese Modelo del Articulo: "
        modelo = confirmacion(msjModelo)
        articulos[int(idArt)]["modelo"] = modelo
    elif opMod == 3:
        msjColor = "Ingrese Color del Articulo: "
        color = confirmacion(msjColor)
        articulos[int(idArt)]["color"] = color
    elif opMod == 4:
        msjPrecio = "Ingrese Precio del Articulo: " 
        precio = confirmacion(msjPrecio)
        while not precio.isdigit():
            print(msjnovalida)
            precio = confirmacion(msjPrecio)
        articulos[int(idArt)]["precio"] = precio
    elif opMod == 5:
        msjCantidad = "Ingresar cantidad de Articulos: "
        cantidad = confirmacion(msjCantidad)
        while not cantidad.isdigit():
            print(msjnovalida)
            cantidad = confirmacion(msjCantidad)
        articulos[int(idArt)]["cantidad"] = cantidad
    else:
        valorN(opMod)
        

