<<<<<<< HEAD
def ventas():
    return None
"""from Inventario import *
from Validador import *

caja={}
def ventas():
    clave = ingresarOpcion()
    clave = validarVenta(clave,"ingrese el ID del articulo")
    #id=int(input("ingrese el numero del articulo: "))
  
=======
from Inventario import *
>>>>>>> 8647d080a71f575e9f3d3d0e3c23469a27d6d850



#not option.isdigit() or

def validarVenta(option,msj):
    while  int(option) not in articulos.keys():
        print("ingrese un id valido")
        option=input(msj)
    return option

def validarCantidad(option,msj, id):
    while option>articulos[int(id)]["cantidad"]:
        print("la cantidad supera al stock disponible")
        option=input(msj)

    return option

def ingresarUnidades(clave):
    unidades=int(input("ingrese el numero de unidades vendidas: "))
    clave=validarCantidad(unidades,"ingrese el numero de unidades vendidas",clave)
<<<<<<< HEAD
    articulos[clave]["Cantidad"]-=unidades
   """ 
=======
    articulos[clave]["cantidad"]-=unidades
    
>>>>>>> 8647d080a71f575e9f3d3d0e3c23469a27d6d850

    
   # print(articulos[id]["Cantidad"])
    

