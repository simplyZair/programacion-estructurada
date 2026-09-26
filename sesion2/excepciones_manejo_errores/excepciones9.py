try:
    edad = int(input("Ingrese su edad: "))
    if edad < 0 or edad > 120:
        print("Edad fuera de rango válido.")
    else:
        print(f"Edad registrada: {edad}")
except ValueError:
    print("Debe ingresar un número entero.")
 