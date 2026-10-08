notas_altas = 0
promedio = 0

for calificacion in range(1, 11):
    nota = int(input("Calificaciones entre 1 y 5: "))
    promedio += nota
    if nota < 1 or nota > 5:
        print("Nota inválida, ingrese una calificación entre 1 y 5")
    elif nota >= 4:
        notas_altas += 1

promedio /= 10
print(f"El promedio es: {promedio}")
print(f"El número de notas altas es: {notas_altas}")
