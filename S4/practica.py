def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal

def aplicar_descuento(subtotal):
    if subtotal >= 3000:
        return subtotal * 0.08
    return 0.0

def calcular_iva(monto_con_descuento):
    return monto_con_descuento * 0.15

# Procedimiento que muestra el resumen
def mostrar_resumen(producto, subtotal, descuento, iva, total):
    print("\n--- RESUMEN DE LA COMPRA ---")
    print(f"Producto: {producto}")
    print(f"Subtotal: C$ {subtotal:.2f}")
    print(f"Descuento (8%): C$ {descuento:.2f}")
    print(f"IVA (15%): C$ {iva:.2f}")
    print(f"Total a pagar: C$ {total:.2f}")

def main():
    producto = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    # Variables locales
    subtotal = calcular_subtotal(precio, cantidad)
    descuento = aplicar_descuento(subtotal)
    monto_con_descuento = subtotal - descuento
    iva = calcular_iva(monto_con_descuento)
    total = monto_con_descuento + iva

    mostrar_resumen(producto, subtotal, descuento, iva, total)

# Ejecución
main()