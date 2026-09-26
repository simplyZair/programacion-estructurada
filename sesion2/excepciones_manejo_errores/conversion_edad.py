try:
    edad = int(input("Edad: "))
except ValueError:
    print("Debe ingresar un número entero.")
else:
    print("Edad registrada:", edad)