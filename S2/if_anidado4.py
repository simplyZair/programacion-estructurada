print("¿El Cliente viene en temporada baja? (Si/No)")
if input().lower() == "si":
    print("Cuantos dias va a reservar el cliente?")
    if int(input()) < 3:
        print("Tiene un descuento del 10%")
    elif int(input()) >= 3 :
        print("Tiene un descuento del 20%")