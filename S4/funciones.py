#Variable Local

def calcular_pago(horas, tarifa):
    pago = horas * tarifa
    print("Pago dentro de la función: C$", pago)


calcular_pago(40, 120)

# La siguiente instrucción produciría NameError:
# print(pago)

#Variable Global
ventas_registradas = 0


def registrar_venta():
    global ventas_registradas
    ventas_registradas += 1
    print("Venta registrada")


registrar_venta()
registrar_venta()

print("Total de ventas:", ventas_registradas)

#Ámbito de las funciones
#Una función declarada en el nivel principal puede llamarse después de su definición. Una función declarada dentro de otra solamente está disponible en el ámbito que la contiene.

def procesar_venta(subtotal):
    def calcular_iva():
        return subtotal * 0.15

    iva = calcular_iva()
    return subtotal + iva


total = procesar_venta(2000)
print("Total: C$", total)

# calcular_iva() no está disponible fuera de procesar_venta.

#Crea una función que reciba un salario numérico, aumente su parámetro y comprueba si cambió la variable original.
#Crea una función que reciba una lista de ventas y agregue una nueva venta mediante append().
#Explica por qué los dos ejercicios producen comportamientos diferentes.

def salario_numerico(salario):
    salario = salario + 1000
    return salario

salario_original = 5000
nuevo_salario = salario_numerico(salario_original)

print("Salario original:", salario_original)
print("Nuevo salario:", nuevo_salario)

def agregar_venta(lista_ventas, nueva_venta):
    lista_ventas.append(nueva_venta)

ventas_originales = [100, 200, 300]
agregar_venta(ventas_originales, 400)
print("Ventas originales:", ventas_originales)