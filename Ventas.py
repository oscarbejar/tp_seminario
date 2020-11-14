from Validador import *
from Inventario import *

caja = {}

def validarVenta():
    msjnovalida = "********¡Tipo de Dato no valido!***********\n" 
    msjID = "Ingresar ID del Articulo : "
    option = confirmacion(msjID)
    while not option.isdigit():
        print(msjnovalida)
        option = confirmacion(msjID)
    
    while int(option) not in articulos.keys():
        print("*****ID ingresado no exite*****")
        option = confirmacion(msjID)
    return option
    
def ingresarUnidades(clave):
    print("\nCantidad en Stock actualmente del articulo: {}".format(articulos[int(clave)]["cantidad"]))
    unidades= input("ingrese el numero de unidades vendidas: ")
    cant = validarCantidad(unidades,"ingrese el numero de unidades vendidas: ",clave)
    articulos[int(clave)]["cantidad"] -= int(cant)
    print("\nActualizando información...\n")
    print("Cantidad de Stock actualizada: {}".format(articulos[int(clave)]["cantidad"]))
    

def validarCantidad(cant,msj, id):
    while int(cant) > articulos[int(id)]["cantidad"]:
        print("*****La Cantidad supera al Stock Disponible*****")
        cant=input(msj)

    return cant


def ingresarUnidades(clave):
    registroVenta=0
    unidades=int(input("ingrese el numero de unidades vendidas: "))
    unidades = validarCantidad(unidades,"ingrese el numero de unidades vendidas",clave)
    articulos[int(clave)]["cantidad"]-=int(unidades)
    registroVenta+=1
    caja = {registroVenta:{id:int(clave),"marca":articulos[int(clave)]["marca"],"unidades": int(unidades)}}
    print("\nGenerando reporte...\n")
    print("Regsistro de la venta N: {}".format(registroVenta))
    print("ID de articulo: {}".format(int(clave)))
    print("Marca: {}".format(articulos[int(clave)]["marca"]))
    print("Unidades vendidas: {}".format(int(unidades)))
    

    
   # print(articulos[id]["Cantidad"])
    

