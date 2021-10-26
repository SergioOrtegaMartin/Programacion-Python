''' Piedra, papel o tijera

P, A y T

en cada tirada la maquina genera la tirada y el usurio escoge la suya pulsando
la tecla y el pulsar me imprime piedra papel o tijera

en cada tirada (ambos tiran) me dice quien gana a quien

gana el mejor de 3

def captura_tirada()

def tira_maquina()

def mostrar_tirada(maquina, jugador) y nos imprime quien gana

gana(maquina, jugador)

'''


from random import randint


def tira_maquina():
    tirada = randint(1,3)
    if tirada == 1:
        return 'Piedra'
    elif tirada == 2:
        return 'Papel'
    else:
        return 'Tijeras'
        
def captura_tirada():
    tirada_p = input(' Tira: P para piedra, A para papel y T para tijera: ')
    if tirada_p == 'P':
        tirada_p = 'Piedra'
    if tirada_p == 'A':
        tirada_p = 'Papel'
    if tirada_p == 'T':
        tirada_p = 'Tijera'
    return tirada_p
    
def gana(maquina, jugador):
    if maquina == 'Papel' and jugador == 'Piedra':
        cont_m += 1
        
    if maquina == 'Tijera' and jugador == 'Papel':
        cont_m += 1
  
    if maquina == 'Piedra' and jugador == 'Tijera':
        cont_m += 1

    if maquina =='Tijera' and jugador == 'Piedra':
        cont_p += 1

    if tirada_m =='Papel' and tirada_p == 'Tijera':
        cont_p += 1

    if tirada_m =='Piedra' and tirada_p == 'Papel':
        cont_p += 1
    
    return maquina and jugador
    
    

cont_m = 0
cont_p = 0
while cont_m < 3 and cont_p < 3:
    tirada_m = tira_maquina()
    tirada_p = captura_tirada()

    if tirada_p == tirada_m:
        print('Empate')
    else:
        if tirada_m == 'Papel' and tirada_p == 'Piedra':
            print('Gana la maquina esta ronda')
            cont_m += 1
            print('Rondas ganadas por la maquina: ', cont_m)
            print('Rondas ganadas tu: ', cont_p)
        if tirada_m == 'Tijera' and tirada_p == 'Papel':
            print('Gana la maquina esta ronda')
            cont_m += 1
            print('Rondas ganadas por la maquina: ', cont_m)
            print('Rondas ganadas tu: ', cont_p)
        if tirada_m == 'Piedra' and tirada_p == 'Tijera':
            print('Gana la maquina esta ronda')
            cont_m += 1
            print('Rondas ganadas por la maquina: ', cont_m)
            print('Rondas ganadas tu: ', cont_p)
        if tirada_m =='Tijera' and tirada_p == 'Piedra':
            print('Ganas tu esta ronda')
            cont_p += 1
            print('Rondas ganadas por la maquina: ', cont_m)
            print('Rondas ganadas tu: ', cont_p)
        if tirada_m =='Papel' and tirada_p == 'Tijera':
            print('Ganas tu esta ronda')
            cont_p += 1
            print('Rondas ganadas por la maquina: ', cont_m)
            print('Rondas ganadas tu: ', cont_p)
        if tirada_m =='Piedra' and tirada_p == 'Papel':
            print('Ganas tu esta ronda')
            cont_p += 1
            print('Rondas ganadas por la maquina: ', cont_m)
            print('Rondas ganadas tu: ', cont_p)

if cont_m > cont_p:
    print('Gana la maquina el juego')
else:
    print('Ganas tu el juego')
    


