#/CASO PRÁCTICO
#Ordenamiento de latencias
#Tu misión: Solicita 10 latencias de respuesta, guárdalas en una lista y muestra los precios de menor a mayor y luego de mayor a menor.

Latencias = []
for i in range(10):
    latencia = float(input("Latencia: "))
    Latencias.append(latencia)

Latencias.sort()
print("Latencias de menor a mayor: ", Latencias)
Latencias.reverse()
print("Latencias de mayor a menor: ", Latencias)