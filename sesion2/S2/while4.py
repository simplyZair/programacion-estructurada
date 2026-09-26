litros = 8

while litros >= 1:
    consumo_litros = int(input("Litros consumidos en el recorrido: "))
    if consumo_litros > litros:
        print("No hay suficiente combustible para el recorrido")
    else:
        litros -= consumo_litros
        if litros <= 1:
            print("ALERTA: Queda un litro de combustible")

