cliente = {
    "nombre": "María",
    "telefono": "8888-8888"
}

try:
    clave = input("Dato a consultar: ")
    print(cliente[clave])
except KeyError:
    print("Ese dato no está registrado.")