print("_"*50)
print("-"*50)
print("Stock de Empresa")
print("_"*50)
print("-"*50)

cargador = True
while cargador == True:

    producto = input("Ingrese el producto a incluir: ")
    marcaProd = input("Ingrese marca del producto: ")
    nombreProd = input("Ingrese nombre del producto: ")
    cantidadProd = int(input("Ingrese cantidad de productos a incluir: "))

    stock  = dict()

    stock[producto] = {marcaProd,nombreProd,cantidadProd}

    resp = input("Desea agregar un producto?(y/n):")
    if resp != "y":
        cargador = False

for s in stock:

    print("El stock de producto ", s)
    print(stock[s])
