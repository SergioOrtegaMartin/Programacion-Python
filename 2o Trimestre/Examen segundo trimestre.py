'''Define la clase moneda con un atributo de instancia para guardar su valor y
con los metodos necesarios para que el siguiente codigo produzca la salida que se indica

1.a) Define el metodo inicializador con un valor pasado como parametro (Moneda(0.5))

1.b)metodo (__str__) para imprimir la instancia con el formato 'Moneda(n)'

1.c) Metodo mas(otra_moneda) que devuelva un resultado str con el valor suma de los valores de las monedas en euros'''


class Moneda:
    def __init__(self,valor):
        self.valor = valor
        
    def __str__(self):
        return 'Moneda {}'.format (self.valor)
    
    def mas(self, otra_moneda):
        suma = self.valor + otra_moneda.valor
        return '{} Euros'.format(suma)
        
'''2. Queremos programar parte del comportamiento de una maquina de monedas (como las de un aparcamiento, por ejemplo)
capaz de recibir y almacenar diferentes tipos de monedas

2.a) Define la clase maquina con un atributo monedero para almacenar objetos moneda (del ej 1)
El monedero será un dict que tiene como clave el valor de cada tipo de moneda y como valor una lista para almacenar todas
las monedas de dicho valor
inicilizar el monedero de la maquina como un diccionario vacio

2.b) La maquina tiene un metodo inserta(Moneda) al que se le pasa como argumento un objeto moneda.
Si no se ha introducido antes ninguna moneda de ese valor se crea la posicion en el diccionario y se guarda la moneda en una lista
Si ya existen monedas de ese valor se añade el objeto moneda en la lista correspondiente

2.c) Define el metodo valor_total() que devuelve la suma total (float)
del valor de las monedas contenidas en el monedero de la maquina
Total acumulado de la suma de: número de monedas de cada tipo X su valor)

2.d) Define el metodo estado() que imprime un resumen del contenido del monedero,
indicando la cantidad de monedas que contiene de cada valor y el valor total de todas las monedas contenidas en la maquina'''


class Maquina:
    def __init__(self):
        self.monedero = {}
        
    def inserta (self, moneda):
        if moneda.valor in self.monedero:
            self.monedero[moneda.valor].append(moneda)
        else:
            self.monedero[moneda.valor] = [moneda]
    
    def valor_total (self):
        suma = 0
        for valor in self.monedero:
            suma += len(self.monedero[valor])*valor
        return suma
    
    def estado(self):
        print ('Moneda ---  Unidades')
        for valor in self.monedero:
            print (valor, '--', len(self.monedero[valor]) )
        print(self.valor_total())
        
        
'''3. Define la clase animal que se suministra
3.a) Define las subclases perro y gato de tal forma que se produzca una salida como la mostrada para el codigo ejecutado'''
        
class Animal:
    def __init__(self ,especie=None):
        self.especie=especie
    def habla(self):
        pass
    
class Perro(Animal):
    def __init__(self,especie='Perro'):   
        self.especie=especie
    def habla(self):
        print ('guau!')
    

'''4.a) Crear la variable letras asignada a una lista por comprension con todas las letras mayusculas y minusculas,
sabiendo que sus codigos ascii son A=65 ... Z=90  a=97... z=122
Todas las letras estan entre 65 y 122 mmenos del 91 al 96 que no son letras
usar funcion chr(n)'''

letras= [chr(n) for n in range (65,123) if n not in range (91,97) ]


'''4.b) define una variable vocales de tipo conjunto que contenga todas las vocales mayusculas y minusculas'''
vocales={'A','E'} #etc

#4.c Obtener el conjunto completo de consonantes mayusculas y minusculas
todas=set(letras)
consonantes= todas-vocales

