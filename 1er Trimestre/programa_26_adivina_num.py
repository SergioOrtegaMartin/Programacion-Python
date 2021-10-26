'''Escribir un programa que genera un numero aleatorio que hay que
adivinar
te dice si has acertado o si estas por debajo o por encima'''


from random import randint



secreto = randint(1, 100)

'''
print('Adivina un numero entre el 1 y 100')

numero = int(input('Escribe un numero: '))

while secreto != numero:
    if secreto > numero:
        print('Demasiado bajo')
    else:
        print('Demasiado alto')
    
    numero  = int(input('Escribe un numero: '))

if secreto == numero:
    print('Has acertado!')
    
    '''

'''Con 7 intentos'''

print('Adivina un numero entre el 1 y 100')

numero = int(input('Escribe un numero: '))

intento = 7

while secreto != numero and intento > 0 :
    if secreto > numero:
        print('Demasiado bajo.', 'Intentos restantes: ', intento,)
    else:
        print('Demasiado alto.', 'Intentos restantes: ', intento)
    numero  = int(input('Escribe un numero: '))
    intento = intento - 1
if secreto == numero:
    print('Has acertado!')
else:
    print('Te has quedado sin intentos, el número era:', secreto)
    
    


