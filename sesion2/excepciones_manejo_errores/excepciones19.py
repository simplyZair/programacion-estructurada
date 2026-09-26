try:
    with open("reportes.txt", "r") as archivo:
        print(archivo.read())
except FileNotFoundError:
    print("El archivo reportes.txt no existe.")
finally:
    print("Operación finalizada.")
 
 