try:
    ventas = float(input("Ventas: "))
    porcentaje = float(input("Porcentaje de comisión: "))
    print(f"Comisión: {ventas * (porcentaje / 100)}")
except ValueError:
    print("Debe ingresar valores numéricos.")