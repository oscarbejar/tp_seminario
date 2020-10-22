print("Stock de Empresa")

producto = input("Ingrese el producto a incluir: ")
nombreProd = input("Ingrese nombre del producto: ")
cantidadProd = input("Ingrese cantidad de productos a incluir: ")

stock  = dict()

stock [producto] = {nombreProd,cantidadProd}

for s in stock:
    print(s)
    print(stock[s])
