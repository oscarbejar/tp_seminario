from Mensajes import *
from MenuPpl import *
from Validador import *
from Inventario import *
from Ingresos import *
from Modificacion import *

def main():
    mostrarMenuPpl()
    op = ingresarOpcion("Seleccione por favor opcion: ")
    op = validarMenu(op,"Seleccione por favor opcion: ", menuppl)
    msjSeleccionarOpcion(op)

    if op == "1":
        ingresarArt(ingresosArt())
    if op == "2":
        modificarArt()
    if op == "3":
        clave=ingresarOpcion("ingrese el ID del articulo")
        clave=validarVenta(clave,"ingrese el ID del articulo")
        ingresarUnidades(clave)
    if int(op) == len(menuppl):
        pass



bienvenida()
main()
conf = repetirOperacion()
while (conf == "y" or conf == "Y"):
    main()
    conf = repetirOperacion()
verStock()
guardarInventario()
verStock()
despedida()
