try:
    monto = float(input("Monto: "))
    tasa_cambio = float(input("Tasa de cambio: "))
    print(f"Monto en otra moneda: {monto * tasa_cambio}")
except ValueError:
    print("Debe ingresar un número válido para el monto y la tasa de cambio.")
