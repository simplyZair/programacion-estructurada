producto = input("Ingrese el nombre del producto: ")
unidades = int(input("Ingrese las existencias: "))
minimo_reposicion = 5

if unidades < minimo_reposicion:
    print(f"Se debe reponer el producto '{producto}'. Quedan '{unidades}' (minimo requerido: {minimo_reposicion})")
else:
    print(f"El inventario de {producto} es suficiente, quedan {unidades}")