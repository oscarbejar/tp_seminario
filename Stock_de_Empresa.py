from menuPpl import *
from validador import *

def main():
    print("_"*50)
    print("-"*50)
    print("Bienvenido al Sistema de Stock de Empresa Infotravel")
    print("_"*50)
    print("-"*50)

    mostrarMenuPpl()

    msj = "Ingrese opcion: "
    opcion = input(msj)
    res = validar(opcion,msj)
    print(res)
main()