import os

#Estacion 1
# def convertir_a_dolares(cordobas):
#     tasa = 36.80
#     return cordobas / tasa

# os.system("cls")
# monto = float(input("Monto en córdobas: "))
# resultado = convertir_a_dolares(monto)
# print("Equivalente en dólares:", round(resultado, 2))

#Es mejor realizar el redondeo fuera de la funcion
#La funcion debe devolver una tarea exacta, o dedicada
#--------------------------------------------------------

#Estacion 2
# def calcular_subtotal(precio, cantidad):
#     return precio * cantidad

# def aplicar_descuento(subtotal, porcentaje):
#     return subtotal*(1-porcentaje)

# precio = float(input("Precio unitario C$: "))
# cantidad = int(input("Cantidad: "))
# descuento = float(input("Descuento: "))
# subtotal = aplicar_descuento(calcular_subtotal(precio, cantidad), descuento)
# print("Subtotal C$:", subtotal)

#Estacion 3
# def leer_cantidad():
#     while True:
#         try:
#             return int(input("Cantidad: "))
#         except ValueError:
#             print("Ingrese un número entero.")

# os.system("cls")
# cantidad = leer_cantidad()
# print("Dato recibido:", cantidad)

#ValueError al ingresar un valor no numerico, por ejemplo "a" 
#y poder repetir el ciclo hasta que retorne un valor esperado.
#--------------------------------------------------------

# #Estacion 4
# def mostrar_encabezado(nombre_empresa):
#     print("=" * 35)
#     print(nombre_empresa.upper())
#     print("=" * 35)

# resultado = mostrar_encabezado("Cafetería El Buen Sabor")
# print("Valor devuelto:", resultado)
#--------------------------------------------------------


#Estacion 5
# def calcular_total(subtotal, impuesto=0.15):
#     monto_impuesto = subtotal * impuesto
#     total = subtotal + monto_impuesto
#     return total

# print(calcular_total(1000))
# print(calcular_total(1000, 0.10))

