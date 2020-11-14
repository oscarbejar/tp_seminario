from Validador import *


def inventario():
    return None
articulos = {
        0:{"marca":"Nike","modelo":"remera","color":"azul","precio":100,"cantidad":1}
    }
    #{"marca":"Nike","modelo":"remera","color":"azul","precio":100,"cantidad":1}
#f
def guardarInventario():
    with open("datos.txt", "w") as datos:
        datos.write(str(articulos))

def verStock():
    file = open("datos.txt")
    print(file.read())
    file.close


def verArticulo():
    msjnovalida = "********¡Tipo de Dato no valido!***********\n" 
    msjID = "Ingresar ID del Articulo a visualizar : "
    id = confirmacion(msjID)
    while not id.isdigit():
        print(msjnovalida)
        id = confirmacion(msjID)
    while int(id) not in articulos.keys():
        print("*****ID ingresado no exite*****")
        id = int(confirmacion(msjID))
    id = int(id)
    print("\nArticulo ID: {}".format(id))
    print("MARCA: {}".format(articulos[id]['marca']))
    print("MODELO: {}".format(articulos[id]['modelo']))
    print("COLOR: {}".format(articulos[id]['color']))
    print("PRECIO: {}$".format(articulos[id]['precio']))
    print("CANTIDAD DISPONIBLE: {}\n".format(articulos[id]['cantidad']))



