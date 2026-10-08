try:
    opcion = int(input("Seleccione una opción (1-3): "))
except ValueError:
    print("Debe ingresar un número.")
else:
    if opcion == 1:
        print("Opción 1 seleccionada")
    elif opcion == 2:
        print("Opción 2 seleccionada")
    elif opcion == 3:
        print("Opción 3 seleccionada")
    else:
        print("Opción fuera de rango")
 