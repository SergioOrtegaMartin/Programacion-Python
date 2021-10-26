'''Escribir una función en el que introduzco un numero y
me diga si es par o no'''


def par(n):
    if n % 2 == 0:
        return True
    else:
        return False


numero = int(input('Dime un numero y te digo si es par: ' ))

if par(numero):
    print('Es par')

else:
    print('Es impar')



'''def par(n):
    return n % 2 == 0:'''
