''' Programa que pida al usuario un numero indterminado de entradas
hasta que el usuario introduzca un 0. En cada programa el ordenador
debe de de decir si el numero es par o impar'''

x = int(input('Introduce un número: '))
 
while x != 0:
    if x % 2 == 0:
        print('PAR')
    else:
        print('IMPAR')
        
    x = int(input('Introduce un número: '))

print('FIN')




