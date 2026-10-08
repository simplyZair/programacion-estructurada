zona = input("Ingrese la zona del cliente (urbana/rural): ")
peso = float(input("Ingrese el peso del paquete en kg: "))

if zona.lower() == "urbana":
    tarifa_base = 10
    if peso <= 5:
        recargo = 0
    else:
        recargo = 5
    
    total = tarifa_base + recargo
    print(f"Envío Urbano | Tarifa base: C${tarifa_base} | Recargo peso extra: C${recargo} | Total: C${total}")

elif zona.lower() == "rural":
    tarifa_base = 20
    if peso <= 5:
        recargo = 0
    else:
        recargo = 10
    
    total = tarifa_base + recargo
    print(f"Envío Rural | Tarifa base: C${tarifa_base} | Recargo peso extra: C${recargo} | Total: C${total}")

else: 
    print("Zona no válida. Por favor, ingrese 'urbana' o 'rural'.")