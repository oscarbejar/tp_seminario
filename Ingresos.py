from Inventario import *
from Validador import *


"""Metodo que carga un nuevo articulo al sistema de stock en formato de diccionario con los detalles del articulo"""
def ingresosArt():
    msjnovalida = "********¡Tipo de Dato no valido!***********\n" 

    msjID = "Ingresar ID del Nuevo Articulo : "
    idArt = confirmacion(msjID)
    while not idArt.isdigit():
        print(msjnovalida)
        idArt = confirmacion(msjID)
    
    while int(idArt) in articulos.keys():
        print("*****ID ingresado ya exite*****")
        idArt = confirmacion(msjID)

    msjMarca = "Ingrese Marca del Articulo: "
    marca = confirmacion(msjMarca)

    msjModelo = "Ingrese Modelo del Articulo: "
    modelo = confirmacion(msjModelo)

    msjColor = "Ingrese Color del Articulo: "
    color = confirmacion(msjColor)
    
    msjPrecio = "Ingrese Precio del Articulo: " 
    precio = confirmacion(msjPrecio)
    while not precio.isdigit():
        print(msjnovalida)
        precio = confirmacion(msjPrecio)

    msjCantidad = "Ingresar cantidad de Articulos: "
    cantidad = confirmacion(msjCantidad)
    while not cantidad.isdigit():
        print(msjnovalida)
        cantidad = confirmacion(msjCantidad)

    artNv = {int(idArt) : {"marca": marca, "modelo": modelo,"color": color,"precio": precio,"cantidad": int(cantidad) }}
    return artNv


"""Metodo que actualiza el diccionario de articulos"""
def ingresarArt(artNv):
    print("\nGuardando nuevo articulo...\n")
    print("\nGUARDADO\n")
    articulos.update(artNv)
    return None






        