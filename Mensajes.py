from MenuPpl import *
from Ingresos import *
from Mensajes import *

def bienvenida():
    print("_"*60)
    print("-"*60)
    print(("       Bienvenido al Sistema de Stock de la Empresa         ").upper())
    print(" ___________________________________________________________ ")
    print("|                                                           |")
    print("|     22222       22222222    22222222      2222    2222    |")
    print("|    22 22      22      22   22      22   22   22 22  22    |")
    print("|   22 22      22      22    2222222     22     2    22     |")
    print("|  22 222222  22      22  22      22    22          22      |")
    print("| 222222222   22222222     2222222     22          22       |")
    print("|___________________________________________________________|")
    print("_"*60)
    print("-"*60)
    print("")

def despedida():
    print("_"*60)
    print("-"*60)
    print(("Programa finalizado").upper())
    print("_"*60)
    print("-"*60)


def mostrarMenuPpl():
    print("-"*60)
    print("Menu Principal de Opciones: ")
    print("-"*60)
    for o in menuppl:
        print(o ,"-", menuppl[o],"\n")

def msjSeleccionarOpcion(op):
    print("_"*60)
    print("-"*60)
    print("\n{}".format(menuppl[int(op)]).upper())
    print("_"*60)
    print("-"*60)

def mostrarProg():
        op = ingresarOpcion("Seleccione por favor opcion: ")
        op = validarMenu(op,"Seleccione por favor opcion: ", menuppl)
        msjSeleccionarOpcion(op)

        if op == "1":
            ingresarArt(ingresosArt())
            guardarInventario()
        if op == "2":
            print("Stock actual")
            verStock()
        if op == "3":
            verArticulo()
        if op == "4":
            modificarArt()
            guardarInventario()
        if op == "5":
            clave = validarVenta()
            ingresarUnidades(clave)
            guardarInventario()
        if int(op) == len(menuppl):
            pass