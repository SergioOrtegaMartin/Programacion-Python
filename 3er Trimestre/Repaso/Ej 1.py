'''1. Crear un programa que abra un fichero en modo escritura,
si no existe lo creará y añadir la frase "Este es el ejercicio1"'''


f = open('Ejercicio1.txt', 'w+') #El w+ es para que no machaque el archivo, si fuera solo w lo machaca
f.write('Este es el ejercicio 1')
f.close()  #Hay que cerrarlo para que lo guarde