numero_alertas = 0
alertas = []

for producto in range (1, 9):
    nombre = input("Nombre del producto : ")
    existencia = int(input("Existencia: "))
    if existencia < 10:
        alertas.append(f"El producto {nombre} tiene {existencia}, reabastecer")
        numero_alertas += 1

print("Productos por reabastecer: ", numero_alertas)

for alerta in alertas:
    print(alerta)