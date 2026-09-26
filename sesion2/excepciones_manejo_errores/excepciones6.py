try: 
    precio_producto = float(input("Precio C$: "))
    print(f"Precio registrado: {precio_producto:.2f}")
except ValueError:
    print("Debe ingresar un número.")