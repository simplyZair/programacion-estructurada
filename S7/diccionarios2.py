directorio = {
    "Juan": "505-1234",
    "María": "505-5678",
    "Pedro": "505-9012"
}

buscar_nombre = "María"

if buscar_nombre in directorio: 
    print("Telefono: ", directorio[buscar_nombre])
else:
    print("Nombre no encontrado en el directorio.")