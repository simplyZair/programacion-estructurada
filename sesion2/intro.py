import keyword
#Lista las palabras reservadas de Python
print("LISTA DE PALABRAS RESERVADAS DE PYTHON")
print(keyword.kwlist)

#Verifica si un token es una palabra reservada o no.
print("¿while es una palabra reservada? Respuesta = "+ str(keyword.iskeyword 
                                                           ("while")))
print("¿estudiante es una palabra reservada? Respuesta = "+ str(keyword.iskeyword
                                                                ("estudiante")))

x = 8
y = 3
z = x/y