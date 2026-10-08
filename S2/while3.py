total = 0
unidades = 0

while unidades < 1 or unidades > 100:
    unidades = int(input("Unidades: "))

total += unidades
print(f"Total: {total}")