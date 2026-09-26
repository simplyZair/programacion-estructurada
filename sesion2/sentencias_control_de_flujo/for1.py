venta_total = 0

for venta in range (1, 8):
    monto = float(input("Ingrese las ventas de la semana, dia por dia: "))
    venta_total += monto
    promedio = venta_total / 7
    
print("El total semanal de ventas es: C$", venta_total)
print("El promedio de ventas es: C$", promedio)