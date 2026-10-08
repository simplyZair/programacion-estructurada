calificacion = 0

try:
    calificacion = int(input("Ingrese la calificación: "))
    if calificacion < 0 or calificacion > 100:
            print("Error: La calificación debe estar entre 0 y 100.")
    elif calificacion >= 0 and calificacion <= 100:
            print(f"La calificación ingresada es: {calificacion}")
    
except ValueError:
    print("Error: Debe ingresar un número entero.")
    