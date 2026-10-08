intentos = 0
clave = ""

while clave != "1234":
    clave = input("Ingrese la clave: ")
    intentos += 1

print("Fueron necesarios ", intentos, "para ingresar")