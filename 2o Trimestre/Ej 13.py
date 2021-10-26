'''Definir coches.
cada cochce tendra una marca y un modelo
La marca y el modelo se puede crear de forma interactiva (pidiendolo)
cada coche va a tener un numero y ese numero se va a crear consecutivamente a partir de un contador
(contar cuantos coches se han creado)
ese contador tenemos que guardarlo dentro de la clase coche '''

#c) Crear otra variable de clase que sean diccionarios donde vamos a guardar las marcas y los modelos que tenemos
#d) Definir estado del coche (parado, arrancado, movimiento)
#definir metodo arrancar(cambia el estado), acelerar(aumenta velocidad de 5 en 5) y frenar (disminuye velocidad de 5 en 5)

#definir el metodo str de tal forma que podamos ver siempre el estado del coche 

import random

class Coche:
    contador=0
    dic={'Alfa':'33', 'Ford' : 'Sierra', 'Fiat' : 'Multipla' , 'BMW' : '320'}
    def __init__(self,mar, mod):
        self.marca=mar
        self.modelo=mod
        Coche.contador += 1
        #dself.arrancado = False
        #self.parado = True
        #sel.velocidad = 0
        
    def __str__(self):    #Sirve para hacer una ersi´pon imprimible de un objeto 
        Coche(mar,mod)

c=Coche(input('Introduce la marca: '),input('introduce el modelo: '))
c2=Coche(input('Introduce la marca: '),input('introduce el modelo: '))
       
  
print('Has creado',Coche.contador, 'coches')


dic={'Alfa':['33','159','Giulia','Brera'], 'Ford' : 'Sierra', 'Fiat' : 'Multipla' , 'BMW' : '320'}

lismar=list(dic.keys())
lismod=list(dic.values())


