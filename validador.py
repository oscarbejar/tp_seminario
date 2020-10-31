def validar(option, msj):
    while option != 1 and option != 2 and option != 3 and option != 4:
        print("Opción no valida")
        print(msj,end=": ")
        option = int(input())
    return option
    
    