limite_credito = 500
registrado = input("Es un cliente registrado? (si/no): ")

if registrado.lower() == "si":
    saldo_pendiente = float(input("Ingrese el saldo pendiente: "))
    if saldo_pendiente > limite_credito:
        print("No se puede realizar la compra, el saldo pendiente es mayor a 500.")
    else:
        print("Se puede realizar la compra.")
else:
    print("No esta registrado, no puede realizar la compra.")