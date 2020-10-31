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
    menup = menuPpl()
    for v in menup:
        print(v , menup[v],"\n")