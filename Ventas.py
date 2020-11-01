from Inventario import *
from Validador import *
caja={}
def ventas():
    clave=ingresarOpcion("ingrese el ID del articulo")
    clave=ValidarVenta(clave,"ingrese el ID del articulo")
    #id=int(input("ingrese el numero del articulo: "))
  

    unidades=int(input("ingrese el numero de unidades vendidas: "))
    clave=validarCantidad(unidades,"ingrese el numero de unidades vendidas",clave)
    articulos[clave]["Cantidad"]-=unidades
    
ventas()
    
   # print(articulos[id]["Cantidad"])
    

