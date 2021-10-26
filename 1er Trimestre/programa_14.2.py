

def cuadrado(x):
    ''' devuelve el cuadrado del valor introducido'''
    return x ** x


def leer_limite():
    '''devuelve el valor entero introducido desde teclado'''
    n = int(input('cuantos cuadradados quieres'))
    return n


limite = leer_limite()

for i in range(1, limite+1):
    print(i, '-->', cuadrado(i))

