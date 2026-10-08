unidades = 3

while unidades < 20:
    agregar_unidades = int(input("Agregar al inventario: "))
    if agregar_unidades <= 0:
        print("Digite un número positivo")
    else:
        unidades += agregar_unidades
        print(f"Inventario actual: {unidades}")
