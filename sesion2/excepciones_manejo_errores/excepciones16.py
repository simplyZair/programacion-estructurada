productos = ["Café", "Azúcar", "Harina", "Sal"]
 
try:
    posicion = int(input("Ingrese la posición a consultar: "))
    print(productos[posicion - 1])
except ValueError:
    print("Debe ingresar un número entero.")
except IndexError:
    print("La posición está fuera del rango de la lista.")
 