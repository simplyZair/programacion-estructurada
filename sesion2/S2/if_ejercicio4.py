recargo = 40
montoPedido = float(input("Ingrese el monto del pedido: "))

if montoPedido < 300:
    montoFinal = montoPedido + recargo
    print(f"El pedido no supera los 300, el monto a pagar con recargo es: {montoFinal}")
else:
    montoFinal = montoPedido
    print(f"El monto a pagar es: {montoFinal}")