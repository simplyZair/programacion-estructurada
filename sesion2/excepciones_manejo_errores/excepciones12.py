try:
    monto = float(input("Monto: "))
    base = float(input("Base: "))
    porcentaje = (monto / base) * 100
    print(f"Porcentaje: {porcentaje}%")
except ValueError:
    print("Debe ingresar un número válido para el monto y la base.")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")