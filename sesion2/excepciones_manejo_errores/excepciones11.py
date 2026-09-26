ventas = []

try:
    venta1 = float(input("Venta 1: "))
    venta2 = float(input("Venta 2: "))
    venta3 = float(input("Venta 3: "))
    promedio = (venta1 + venta2 + venta3) / 3
    print(f"Promedio de ventas: {promedio}")
except ValueError:
    print("Debe ingresar un número válido para las ventas.")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")

    