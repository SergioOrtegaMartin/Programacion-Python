''' Escribir una función que le mando un numero y me devuelve el cuadrado'''


def cuadrado(x): #la n se copia en x 
    return x ** 2

n = int(input(' Escribe un numero y lo elevo al cuadrado hasta ese numero: '))

print(cuadrado(n))

print()



    
    
'''b. que imprima el cuadradado de los 100 primeros numeros'''

for i in range(1,n + 1):
    print(i, '-->', cuadrado(i))

print()


def leer_limite():
    n = int(input(' cuantos cuadrados quieres '))

    
