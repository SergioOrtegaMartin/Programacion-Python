'''definir la funcion dado
esta funcion devuelve un numero comprendido entre 1 y 6 


b. simular una tirada de dos dados de un jugador de la maquina
el programa tiene que decir la tirada de la maquina de los dos dados
y la suma
maquina: 5 y 5 total: 10
pulsa enter para tirar (enter)
jugador: 5 y 6 total: 11
y que nos diga quien ha ganado



utilizar una variable acumulador para la maquina y otro para el jugador
'''


from random import randint


def dado():
    return randint(1,6)
 


d1 = dado()
d2 = dado()
d_maquina = d1 + d2

print('maquina:',d1, 'y', d2, 'total:', d_maquina)

print()

input('Pulsa enter para tirar un dado:')


d3 = dado()
d4 = dado()
d_persona = d3 + d4


print()

print('Tu tirada:',d3, 'y', d4, 'total:', d_persona)

print()

if d_maquina == d_persona:
    print('Empate')

if d_maquina > d_persona:
    print('Has perdido')
else:
    print('Has ganado!')

print() 

''' modificar el programa para que juege la maquina contra el jugador pero
gana el primero que llegue a 100 de la suma de las tiradas'''

##d_persona = 0
##d_maquina = 0
##while d_persona < 20 and d_maquina < 20:
##    d1 = dado()
##    d2 = dado()
##    d_maquina = d_maquina + d1 + d2
##    print('maquina:',d1, 'y', d2, 'total:', d_maquina)
##    print()
##    d3 = dado()
##    d4 = dado()
##    if d_maquina < 20:
##        input('Pulsa enter para tirar un dado:')
##        d_persona = d_persona + d3 + d4
##        print('Tu tirada:',d3, 'y', d4, 'total:', d_persona)
##        print()
##
##if d_persona > 20:
##    print('Has ganado')
##else:
##    print('Gana la maquina')
##    
    
''' Considerar tanto como la maquina y el jugador debe de tirar el mismi
numero de veces y gana el de mas puntuacion'''


def estado(juega, d1, d2):
        print(juega ,d1, 'y', d2, 'total:', d1 + d2)

LIMITE = 20


d_persona = 0
d_maquina = 0
while d_persona < LIMITE and d_maquina < LIMITE:
    dado1 = dado()
    dado2 = dado()
    d_maquina += dado1 + dado2
    estado('maquina', dado1, dado2)
    
    print()
    
    dado1 = dado()
    dado2 = dado()
    d_persona += dado1 + dado2
    input('Pulsa enter para tirar un dado:')
    estado('jugador', dado1, dado2) 
    print()

    print('La maquina lleva: ', d_maquina)
    print('Tu llevas: ', d_persona)

    print()


if d_persona > d_maquina:
    print('Has ganado')
else:
    print('Gana la maquina')

