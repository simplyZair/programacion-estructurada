ventas = []
try:
    for i in range(1, 4):
        venta = float(input(f"Venta {i}: "))
        ventas.append(venta)
    promedio = sum(ventas) / len(ventas)
    print(f"Promedio: {promedio}")
except ValueError:
    print("Debe ingresar solo números.")
except ZeroDivisionError:
    print("No hay datos para calcular el promedio.")
 