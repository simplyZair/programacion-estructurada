empleados = {"E001": "Juan Pérez", "E002": "Ana López"}
clave = input("Ingrese la clave del empleado: ")
 
try:
    print(empleados[clave])
except KeyError:
    print("Empleado no encontrado.")

#print(empleados.get(clave, "Empleado no encontrado."))