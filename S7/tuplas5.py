def analizar_ventas (ventas):
    total = sum(ventas)
    promedio = total / len(ventas)
    venta_maxima = max(ventas)

    return total, promedio, venta_maxima

lista_de_ventas = [100, 200, 150, 300, 250]
total, promedio, venta_maxima = analizar_ventas(lista_de_ventas)

print(f"Total de ventas: C$ {total:.2f}")
print(f"Promedio de venta: C$ {promedio:.2f}")
print(f"Venta máxima: C$ {venta_maxima:.2f}")