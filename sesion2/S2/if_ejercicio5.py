entrega_esperada = 46
numero_sacos = float(input("Ingrese el numero de sacos: "))

if numero_sacos == entrega_esperada:
    print("La entrega esta completa.")
elif numero_sacos > entrega_esperada:
    diferencia = numero_sacos - entrega_esperada
    print(f"Se han recibido {diferencia} sacos de mas.")
else:
    diferencia = entrega_esperada - numero_sacos
    print(f"Debe revisarse, faltan {diferencia} sacos.")