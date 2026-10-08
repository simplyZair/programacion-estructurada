import os

tasa_cambio = 36.72

def imprimirDatos(cif,nombre,promedio,becado):
    if (promedio >= 80) and (becado==True):
        estatus="Renovado"
    elif (promedio < 80) and (becado==True):
        estatus= "Revocado"
    else:
        estatus="No becado"

    os.system("cls")
    print("DATOS DEL ESTUDIANTE")
    print("*"*15)
    print(f"CIF: {cif}")
    print(f"Nombre: {nombre}")
    print(f"Promedio: {promedio}")
    print(f"Estado de Beca: {estatus}")
    print("*"*15)

def leerDatos():
    print("//////// Registro de Estudiantes ////////")
    cif=input("Ingrese el CIF del estudiante: ")
    nomb=input("Ingrese el nombre completo del estudiante: ")
    prom=float(input("Ingrese el promedio del estudiante: "))
    beca=input("¿El estudiante es becado? (S/N): ")
    if(beca.strip().upper()=="S"):
        beca=True
    else:
        beca=False
    return cif,nomb,prom,beca