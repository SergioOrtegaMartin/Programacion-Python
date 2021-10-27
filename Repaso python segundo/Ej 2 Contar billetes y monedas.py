#Una funcion a la que le pasamos una cantidad y nos hace el desglose en monedas
import math
diccionario = {500:0 , 200:0 , 100:0 , 50:0 , 20:0 , 10:0 , 5:0 , 2:0 , 1:0 , 0.5:0 , 0.2:0 , 0.1:0 , 0.05:0 , 0.02:0 , 0.01:0}

cantidad= float(input ('¿Cuanto dinero tienes?: '))

def contardinero(cantidad):
    for e in diccionario:
        diccionario[e] = math.floor(cantidad // e)
        cantidad = cantidad % e 

contardinero(cantidad)

suma= 0

for e in diccionario:
    suma += e * diccionario[e]
    
if cantidad - suma != 0 :
    diccionario[0.01] =+1
    
for e in diccionario:
    if diccionario[e] !=0 :
        print ('Tienes ' + str(diccionario[e]) + ' de ' + str(e))


 