existencias = [5, 10, 0, 2, 4, 0]
agotados = 0

for i, existencia in enumerate(existencias):
    if existencia == 0:
        print(f"Productos agotados: {i+1}")
        agotados += 1

print(f"Total de productos agotados: {agotados}")