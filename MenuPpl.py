from Inventario import *

def menuPpl():
    menuppl = {
        1: "Ingresar Articulos",
        2: "Editar Articulos",
        3: "Eliminar Articulo",
        4: "Salir del Sitema"
}
    return menuppl

def seleccion(op):
    if op == "1":
        ingresos()
    if op == "2":
        inventario()
    if op == "3":
        Ventas()