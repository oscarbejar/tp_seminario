


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
    registroVenta=0
    unidades=int(input("ingrese el numero de unidades vendidas: "))
    clave=validarCantidad(unidades,"ingrese el numero de unidades vendidas",clave)
    articulos[clave]["cantidad"]-=unidades
    registroVenta+=1
    caja={registroVenta:{articulos[int(id)]["marca"]}}
    print(caja.keys())
    print("chau oscar")
    
    

    
   # print(articulos[id]["Cantidad"])
    

