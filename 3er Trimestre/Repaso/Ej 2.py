'''2. Crear un programa que abra el fichero editado anteriormente y muestre el
estado del fichero, el modo en el que fue abierto, el nombre y la codiciacion de caracteres del mismo'''

#Abribos el fichero
f = open('Ejercicio1.txt', 'r+')


#Obtenemos los datos del fichero
nombre= f.name
modo= f.mode
encoding= f.encoding

#Cerramos el fichero
f.close

#Imprimimos los datos
print(nombre)
print(modo)
print(encoding)