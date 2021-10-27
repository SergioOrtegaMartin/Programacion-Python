'''Tenemos una matriz bidimensional con un numero de filas (f) y columnas (c).
Escribe una funcion que tome como parametros esa matriz y devuelva una matriz de salida donde esten invertidas todas las posiciones en filas y en columnas'''

'''        '''

matriz= [[1,2,3],[4,5,6],[7,8,9]]


def invertir_columnas(matriz):
    columnasinvertidas = list(reversed(matriz))
    
    return columnasinvertidas

#devuelve: [[7, 8, 9], [4, 5, 6], [1, 2, 3]]


def invertir_filas(columnasinvertidas):
    final = []
    contador = 0
    for e in columnasinvertidas:
        final.append(list(reversed(columnasinvertidas[contador])))
        contador += 1
    return final
       
    
a=invertir_columnas(matriz)
b=invertir_filas(a)

print(b)

'''Python permite usar referencias a funciones nativas (objetos funcion) x= abs
>>> x(-5)
Queremos aplicar una serie de acciones (funciones) sobre una lista de datos, estas acciones
modificarán el contenido de la lista y serán acumulativas
a) Escribe una funcion 'aplica(f, datos)' que aplique una funcion a la lista de datos
b) Escribe una funcion 'procesa(lista_de_acciones, lista_de_datos) a la que se le pasan la lista
de funciones que hay que aplicar (como una lista)


'''







