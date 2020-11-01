from Inventario import *
from Ingresos import *
from Ventas import *
from Modificacion import *

def menuPpl():
    menuppl = {
        1: "Ingresar Articulos",
        2: "Modificar Articulos",
        3: "Ventas",
        4: "Salir del Sitema"}
    return menuppl

def seleccion(op):
    if op == "1":
        ingresos()
    if op == "2":
        modificacion()
    if op == "3":
        ventas()