nombre = input("Ingrese su nombre: ")

try: 
    edad = int(input("Edad: "))
except ValueError:
    print("Debe ingresar un número entero.")

try:
    salario = float(input("Salario: "))
except ValueError:
    print("Debe ingresar un número válido para el salario.")