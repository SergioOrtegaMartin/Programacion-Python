''' Escribir una funcion que saque una tirada aleatoria de una moneda
la funcin devuelve cara o cruz
funcion se llama tira_moneda

juego contra la maquina: gana el que llegue a antes a 3 caras

nosotros pulsamos cualquier tecla para tirar'''

from random import randint


def tira_moneda():
    if randint(1,2) == 1:
        return 'cara'
    else:
        return 'cruz'
    


contador_maquina = 0

contador_persona = 0


while contador_maquina < 3 and contador_persona < 3:
    tiro = tira_moneda()
    print('Maquina: ', tiro,)
    if tiro == 'cara':
        contador_maquina += 1
        print('Aciertos del PC: ', contador_maquina)
    input('Tira pulsando cualquier tecla')
    tiro = tira_moneda()
    print('Tu tirada:', tiro)
    print()
    if tiro == 'cara':
        contador_persona += 1
        print('Aciertos tuyos: ', contador_persona)

if contador_maquina > contador_persona:
    print('Gana la maquina')

else:
    print('Ganas tu')
    
    



















 
