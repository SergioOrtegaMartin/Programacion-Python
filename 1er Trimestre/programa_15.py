''' escribir una función a la que pasamos como parametro dos valores
un numero y una potencia
funcion le llamamos elevado
elevado(n,potencia)
la funcion nos debe de devolver el numero elevado a la potencia

(3,2) 3**2'''



def elevado(x,y):
    return x ** y



''' la funcion leer limite le pasamos un texto y la funcion mostrara ese
texto al usuario y captura un valor numero convertido en numerico


lee_int(texto)

tecxto = ' introduce un numero'
'''

def lee_entero(texto):
    '''captura y convertir a int entrada'''
    x = int(input(texto))
    return x 

n = lee_entero('Introduce un numero')
p = lee_entero('Introduce potencia')

print(n, 'elevado a', p, 'es',elevado(n,p))


