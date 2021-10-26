#Define un terremoto con unas coordenadas, una profundidad y una magnitud, puede tener asociado tambien en una lista de daños
#producito a un dia y una hora que será una tupla (d/m/a   h:m:s)
#Para loalizar un terremoto necesitariamos el momento y las coordenadas
#Construir el valor
#Escribir una funcion que devuelva un color asociado a una magnitud
'''de 0 a 2, amarilo
entre 2 y 3 naranja claro
entre 3 y 4 naranja
de 4 hacia arriba rojo'''

import random
def dia():
    dia=random.randint(1, 31)
    return(dia)

def hora():
    hora=random.randint(0, 23)
    return(hora)

def minuto():
    minuto=random.randint(0, 59)
    return(minuto)

def segundo():
    segundo=random.randint(1, 59)
    return(segundo)

def coordenada1():
    coordenada1=random.randint(370, 375)/10
    return(coordenada1)

def coordenada2():
    coordenada2=random.randint(0, 5)
    return(coordenada2)

def magnitud():
    magnitud=random.randint(0, 100)/10
    return(magnitud)

def profundidad():
    profundidad=random.randint(0, 100)/10
    return(profundidad)

def clave(dia,hora,minuto,segundo,coordenada1,coordenada2):
    tupla_fecha=(2021,1,dia,hora,minuto,segundo)
    tupla_coordenadas=(coordenada1,coordenada2)
    tupla_clave=(tupla_fecha,tupla_coordenadas)
    
    return(tupla_clave)
    
def elemento(magnitud, profundidad):
    comentario=input('Algun comentario? ')
    tupla_elemento=(magnitud, profundidad, comentario)
    
    return(tupla_elemento)
    



