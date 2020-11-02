def inventario():
    return None
articulos = {
        1:{"marca":"Nike","modelo":"remera","color":"azul","precio":100,"cantidad":1}
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






