ventas_tecnicos = {
    "Carlos": 1250,
    "Ana": 2100,
    "Pedro": 1850,
    "Sofia": 2100,
    "Luis": 950
}

venta_mayor = 0
mejor_tecnico = ""

for tecnico, venta in ventas_tecnicos.items():
    print(f"{tecnico}: {venta}")
    if venta > venta_mayor:
        venta_mayor = venta
        mejor_tecnico = tecnico

print(f"El mejor tecnico con la venta mayor es {mejor_tecnico} con un total de {venta_mayor}")