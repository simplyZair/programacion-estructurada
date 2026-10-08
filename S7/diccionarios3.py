conteo_accesos = {}
accesos = ["Router", "PC-Admin", "Router", "Switch", "PC-Admin", "Router"]

for dispositivo in accesos:
    count = conteo_accesos.get(dispositivo, 0)
    conteo_accesos[dispositivo] = count + 1

print(conteo_accesos)