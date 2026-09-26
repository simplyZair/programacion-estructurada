total_produccion = 0
total_ventas = 0

for produccion in range(1, 7):
    produccion = int(input("Producción del día: "))
    total_produccion += produccion

for ventas in range(1, 7):
    ventas = int(input("Ventas del día: "))
    total_ventas += ventas

producto_sobrante = total_produccion - total_ventas

print("El total de producción es: ", total_produccion)
print("El total de ventas es: ", total_ventas)
print("El producto sobrante es: ", producto_sobrante)
