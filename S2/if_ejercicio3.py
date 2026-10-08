meta_diaria = 4000
ventas = float(input("Ingrese las ventas del día: "))

if ventas == meta_diaria:
    print("¡Felicidades! Has alcanzado la meta diaria.")
elif ventas > meta_diaria:
    diferencia = ventas - meta_diaria
    print(f"¡Felicidades! Has superado la meta diaria de C${diferencia}.")
else:
    diferencia = meta_diaria - ventas
    print(f"No has alcanzado la meta diaria. Te faltaron C${diferencia}.")
