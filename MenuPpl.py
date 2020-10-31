from Inventario import *
from Ingresos import *
from Ventas import *

def menuPpl():
    menuppl = {
        1: "Ingresar Articulos",
        2: "Editar Articulos",
        3: "Ventas",
        4: "Salir del Sitema"}
    return menuppl

def seleccion(op):
    if op == "1":
        ingresos()
    if op == "2":
        inventario()
    if op == "3":
        ventas()