from Validador import *
from Inventario import *

"""Diccionario donde guardaremos los registros de ventas"""
caja = {}

"""Metodo que valida los datos que se ingresan al momento de registrar una venta"""
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
    
"""Metodo que muestra e indica si hay disponibilidad de cantidad en stock"""
def validarCantidad(cant,msj, id):
    while int(cant) > articulos[int(id)]["cantidad"]:
        print("*****La Cantidad supera al Stock Disponible*****")
        cant=input(msj)

    return cant

"""Metodo que realiza el ingreso y registro de la venta con detalles de la misma y la guarda un diccionario"""
def ingresarUnidades(clave):
    msjValUnd= "ingrese el numero de unidades vendidas: "
    print("\nCantidad en Stock actualmente del articulo: {}".format(articulos[int(clave)]["cantidad"]))
    unidades=int(validarN(input(msjValUnd),msjValUnd))
    unidades = validarCantidad(unidades,msjValUnd,clave)
    articulos[int(clave)]["cantidad"]-=int(unidades)
    registroVenta = len(caja) + 1
    ventas = {registroVenta :{"id":int(clave),"marca":articulos[int(clave)]["marca"],"unidades": int(unidades)}}
    caja.update(ventas)
    print("\nGenerando reporte...\n")
    print("Regsistro de la venta N: {}".format(registroVenta))
    print("ID de articulo: {}".format(int(clave)))
    print("Marca: {}".format(articulos[int(clave)]["marca"]))
    print("Unidades vendidas: {}".format(int(unidades)))

"""Metodo que guarda en un archivo el registro de caja con detalles de la venta"""
def actualizarCaja():
    with open("ventas.csv", "w") as datos:
        datos.write(str(caja))

    

