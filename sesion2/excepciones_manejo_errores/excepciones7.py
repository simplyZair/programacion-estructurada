cantidad = 0
try:
    cantidad = int(input("CANTIDAD : "))
except ValueError:
    print("Error: Por favor, ingrese un número válido.")
    