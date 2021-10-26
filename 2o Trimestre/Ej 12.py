'''Crear una clase Persona que va a tener un nombre y una edad'''
'''Ponerle un método cumpleaños que le sume uno a la edad'''

class Persona:
    def __init__(self,nom):
        self.nombre=nom
        self.edad=0
        self.estado='Dormido'
        self.bebido = False
        self.test_alcohol=0
        
    def saluda(self): #El primer parámetro siempre es self
        if not self.bebido:
            print('Hola me llamo ', self.nombre, 'y tengo ', self.edad, 'años')
        else:
            print('asdfhgdsjhfgjdsfgsdhjgfhjsdgf', self.test_alcohol)
    
    def cumple(self):
        self.edad += 1
    
    def despertar(self):
        self.estado='Despierto'
    
    def bebe(self, num_copas):
        self.bebido = True
        self.test_alcohol += num_copas
    
         
p=Persona('Pepe')
a=Persona('Pepe2')
b=Persona('Pepe3')
c=Persona('Pepe4')
d=Persona('Pepe5')
e=Persona('Pepe6')
f=Persona('Pepe7')
g=Persona('Pepe8')
h=Persona('Pepe9')
i=Persona('Pepe10')

listap=[p,a,b,c,d,e,f,g,h,i]
    
from random import randint

for i in range (170):
    listap[randint(0,len(listap)-1)].cumple()
 
#for i in range (10):
#    listap[i].cumple()
    
for p in listap:
   p.saluda()


for i in range (20):
    listap[randint(0,len(listap)-1)].bebe(randint(1,3))

for p in listap:
    print(p.nombre, p.test_alcohol)










