from calculos import calcular_subtotal
from calculos import aplicar_descuento

subtotal = calcular_subtotal(120, 5)
descuento = aplicar_descuento(subtotal, 10)
total = subtotal - descuento

print("Total C$:", total)