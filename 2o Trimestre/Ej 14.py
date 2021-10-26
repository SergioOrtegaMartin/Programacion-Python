from random import choice

class Coche:
    cont = 0
    
    
    def _init_(self, nom, mod):
       self.nombre = nom
       self.modelo = mod
       Coche.cont = Coche.cont + 1
       self.parado = True            # estado del coche 
       self.arrancado = False
       self.velocidad = 0
    

    
    def acelerar(self):
        self.velocidad = self.velocidad + 5
        
    def frenar(self):
        self.velocidad = self.velocidad - 5
       
    def _str_(self):
        return 'Coche({}, {})'.format(self.nombre, self.modelo)
    
        
    def arrancar(self):
        
        self.arrancado = True
        self.parado = False

            
            
            
listaNom = ['Mercedes','BMW',' Audi','Nissa','Toyota','Renault','Ferrari','Porche','Citroen']

listaMod=  ['Turbo','Flash','Diamante','Oro','Rapidin','Letin','Normal','Exclusivo']

lista = []

for i in range(8):
    lista.append(Coche(choice(listaNom),choice(listaMod)))
  
    
    print(lista[i].nombre, lista[i].modelo)
    

print('Se han creado', Coche.cont, 'modelos')