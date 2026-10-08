peso_total = 0
numero_sacos = []

for saco in range(1, 6):
    peso = float(input("Peso: "))
    numero_sacos.append(f"Saco N° {saco} recibido con {peso} kg")
    peso_total += peso

print("Peso total kg: ", peso_total)
for saco in numero_sacos:
    print(saco)