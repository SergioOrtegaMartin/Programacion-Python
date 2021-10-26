#f=open('prueba.txt')
'''linea=f.readline()   #Asi imprimimos una linea
print(linea)'''

'''contenido=f.read()    #Asi imprimimos el archivo entero
print(f)
print(type(contenido))   #Asi comprobamos que es un str'''

#b) Hacer una lectura por lineas de un fichero de texto e imprimirlo en pantalla
'''linea = f.readline()
while linea != '':
    print(linea)     
    linea = f.readline()'''

'''lineas=f.readlines()
print(type(lineas))    #Imprime las lineas en una lista
print(lineas)'''

#c) Definir una funcion (listarficheros)para que se le pase a un nombre de fichero y esta funcion saca un listado por lineas
#Poner except  si no existe (FileNotFoundError)

def listarfichero(fichero):
    try:
        f = open(fichero)
        linea = f.readline()
        while linea != '':
            print(linea)
            linea = f.readline()
        f.close
    except FileNotFoundError:
        print("Este fichero no existe")

listarfichero('8.txt')

