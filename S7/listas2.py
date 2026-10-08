ventas = [100, 200, 150, 300, 250, 400, 350]

total_ventas = sum(ventas)
promedio = total_ventas / len(ventas)
dia_venta_maxima = ventas.index(max(ventas)) + 1

print(f"Venta Maxima: {max(ventas)}")
print(f"Total de Ventas: {total_ventas}")
print(f"Promedio de Ventas: {promedio}")
