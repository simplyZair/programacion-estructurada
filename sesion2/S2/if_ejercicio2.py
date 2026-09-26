descuento = 0.10
monto_pedido = float(input("Ingrese la cantidad de compra: "))


if monto_pedido > 1500:
    monto_final = monto_pedido - (monto_pedido * descuento)
    print(f"El monto a pagar con descuento es: {monto_final}")
else:
    monto_final = monto_pedido
    print(f"El monto a pagar es: {monto_final}")
