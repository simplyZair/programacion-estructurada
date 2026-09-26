humedad = float(input("Ingrese el porcentaje de humedad del lote (%): "))

if humedad >= 10 and humedad <= 12:
    defectos = int(input("Ingrese la cantidad de defectos en el lote: "))
    if defectos <=3:
        print("El lote entra en la categoria Exportacion (A).")
    elif defectos <= 8:
        print("El lote entra en la categoria Estandar (B).")
    else:
        print("El lote entra en la categoria Baja (C).")
else:
    print("El lote no cumple con los requisitos de humedad para ser clasificado.")
