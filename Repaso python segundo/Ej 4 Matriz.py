'''a) Escribir una funcion que le pasamos el numero de filas y de columnas y devuelva una matriz bidimensional con ese numero
de filas y de columnas '''
import random

def crearmatriz(filas,columnas):
    matriz = []
    for e in range (filas):
        lista = []
        while len(lista) < columnas:
            lista.append(random.randint(1,5))
        matriz.append(lista)
    return matriz

'''b) Una funcion que nos de la suma de las filas de la matriz
sumaFilas(tabla) donde tabla es la matriz.'''

def sumafilas(tabla):
    lista = []
    for e in range(len(tabla)):
        suma.append(sum(tabla[e]))
    return lista

'''c) Otra funcion que suma las columnas'''

def sumaColumnas(tabla):
    numero_columnas = len(tabla[0])
    sumas = []
    for i in range (0, numero_columnas):
        sumaColumna = 0
        for e in range(0, len(tabla)):
            sumaColumna += tabla[e][i]
        sumas.append(sumaColumna)
    return sumas


