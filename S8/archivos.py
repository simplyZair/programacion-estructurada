#fichero = open('ejemplo.txt')
#contenido = fichero.read()
#print(contenido)
#fichero.close()


#fichero = open('S8/ejemplo.txt')
#fila = fichero.readline()
#print(fila)
#fila = fichero.readline()
#print(fila)
#fichero.close()

#fichero = open('S8/estudiantes.txt', 'w')
#fichero.write("12301450\n")
#fichero.write("Luis Fernando Gonzalez\n")
#fichero.write("96.56\n")
#fichero.write("True\n")
#fichero.write("Ingenieria en Sistemas\n")
#fichero.write("100\n")

#fichero.close()

#fichero = open('S8/estudiantes.txt', 'a')
#lista = ["12301451", "Ernesto Javier Jarquin Montes", 
#         "85.75", "True", "Veterinaria", "90"]
#for linea in lista:
#    fichero.write(linea + "\n")
#fichero.close()

fichero = open('S8/estudiantes.txt', 'a')
lista = ["12301451", "Ernesto Javier Jarquin Montes", 
         "85.75", "True", "Veterinaria", "90"]
fichero.writelines(lista)
fichero.close()