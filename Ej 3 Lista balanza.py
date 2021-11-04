'''Escribir una funcion a la que se le pasa una lista de numeros de tamaño n (impar) > 1, tenemos que buscar el punto de la lista
en el que la sublista de la izquierda mide lo mismo que la del lado derecho'''
from random import randint

lista = [6, 4, 6, 3, 2, 5, 5, 6, 5, 4, 6]
#while len(lista) < 11:
#    lista.append(randint(1,10))
    

def balanza(lista):
    pos1 = 0
    pos2 = pos1 + 1 
    parte1 = sum(lista[0:pos1])
    parte2 = sum(lista[pos2:len(lista)])
    contador= 0 
    while contador < len(lista):
        if parte1 != parte2 :
            parte1 = sum(lista[0:pos1])
            parte2 = sum(lista[pos2:len(lista)])
            pos1 += 1
            pos2 = pos1 + 2 
            #print ('La parte 1 es' , parte1, pos1-1)
            #print ('La parte 2 es' , parte2, pos2-1)
            #print(' ')
        else:
            print ("La mitad está en la posicion" ,pos1 )
        contador +=1
