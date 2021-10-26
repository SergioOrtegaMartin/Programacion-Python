''' una función que sea divisible

def funcion (n, divisor)

la funcion devuelve un bool si es V si n es divisible entre divisor'''

numero = int(input('Dime un numero y te digo si es divisible: '))
numero2 = int(input('Dime el divisor: ' ))


print()
def divisible(n, divisor):
    '''Devuelve Trueo False  si nun es divisible por i'''
    return n % divisor == 0
        

'''if divisible(numero, numero2):
    print('Es divisible')

else:
    print('No es divisible')
'''
print(divisible(numero, numero2)) 

print()

''' que nos pida un numero y el programa produce por salida todos los divisores
de ese numero'''


numero = int(input('Dime un numero y te digo sus divisores: ' ))
print()

print('Los divisores de', numero, 'son: ')


for i in range(1, numero + 1):
    if divisible(numero, i):
        print(i)
