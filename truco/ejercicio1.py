#intruduzco datos
cantidad_articulos = int(input("Ingrese la cantidad de artículos a comprar: "))

if cantidad_articulos < 8:
    print("la cantidad de articulos es:",cantidad_articulos)
    print("Por favor, diríjase a la caja rápida")
else:
    print("Por favor, diríjase a la caja normal")
