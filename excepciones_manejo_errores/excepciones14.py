# edad = input("Edad: ")
# resultado = edad + 5   # TypeError: no se puede sumar str + int
# Esto ocurre porque input() siempre devuelve texto (str), y no se
# puede sumar directamente un str con un int sin convertirlo antes.
try:
    edad = int(input("Edad: "))
    print(edad + 5)
except ValueError:
    print("Debe ingresar un número entero.")
 
