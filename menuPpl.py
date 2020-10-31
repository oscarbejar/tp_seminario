def menuPpl():
    menuppl = {
        1: "Ingresar Articulos",
        2: "Editar Articulos",
        3: "Eliminar Articulo",
        4: "Salir del Sitema"
}
    return menuppl

def mostrarMenuPpl():
    print("Menu Principal de Opciones: \n")
    for o in menuPpl():
        print(o , menuPpl()[o],"\n")