from Inventario import *
from Validador import *

def ingresos():
    return None

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

    artNv = {idArt : {"marca": marca, "modelo": modelo,"Color": color,"Precio": precio,"Cantidad": cantidad }}
    return artNv

def ingresarArt(artNv):
    print(articulos)
    articulos.update(artNv)
    print(articulos)
    return None






        