total = 0
venta = float(input("Monto de Venta: "))

while venta != 0:
    total += venta
    venta = float(input("Monto de Venta: "))

print(f"Total C$: {total}")