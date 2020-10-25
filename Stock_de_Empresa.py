print("_"*50)
print("-"*50)
print("Stock de Empresa")
print("_"*50)
print("-"*50)

cargador = True
while cargador == True:

    id = int(input("Ingrese el id de producto a incluir: "))

    idProd = []

    if id not in idProd:
        idProd.append(id)
        marcaProd = input("Ingrese marca del producto: ")
        nombreProd = input("Ingrese nombre del producto: ")
        colorProd = input("Ingrese color del producto: ")
        cantidadProd = int(input("Ingrese cantidad de productos a incluir: "))

    stock  = dict()

    stock[id] = {marcaProd,nombreProd,colorProd,cantidadProd}

    resp = input("Desea agregar un producto?(y/n):")
    if resp != "y":
        cargador = False

for s in stock:

    print("\n El stock de producto id: ", s)
    print(stock[s])

print("-"*50)
print("programa finalizado")
print("-"*50)