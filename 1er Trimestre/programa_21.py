'''Se le pasa una cadena de caractereces y la devuelve
quitandole los blancos'''

def sin_blanco(cadena):
    x = ''
    for c in cadena:
        if c != ' ':
            x = x + c
    return x


print(sin_blanco('hola, jose maria'))

print()

texto = input('Escribe algo:')

print()

print(sin_blanco(texto))
        
