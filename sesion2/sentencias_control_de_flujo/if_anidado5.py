tipo_cliente = input("Ingrese el tipo de cliente (mayorista/minorista): ")
if tipo_cliente.lower() == "mayorista":
    cantidad = int(input("Ingrese el monto de su compra: "))
    if cantidad >= 1000:
        print("Alcanza la compra minima, tiene un descuento del 15%")
        print("Su total es: C$", cantidad * 0.85)
    else:
        print("Su total es: C$", cantidad)

elif tipo_cliente.lower() == "minorista":
    cantidad = int (input("Ingrese el monto de su compra: "))
    if cantidad >= 500:
        print("Alcanza la compra minima, tiene un descuento del 10%")
        print("Su total es: C$", cantidad * 0.90)
    else:
        print("Su total es: C$", cantidad)
