inventario = {
    "manzanas": 50,
    "bananas": 30,
    "naranjas": 25
}

inventario["manzanas"] = inventario["manzanas"] + 20
inventario["bananas"] = inventario["bananas"] - 20
inventario["naranjas"] = inventario["naranjas"] + 10

for producto, existencia in inventario.items():
    print(f"{producto}: {existencia}")