'''Escribir una funcion que se la pasa una cadena
y se le pasa la cadena inversa'''


def inversa(cadena):
    resul = ''
    for i in range (len(cadena)):
        resul = cadena[i] + resul
    return resul

x = input('Dime una palabra: ')

print(inversa(x))


'''otra forma de hacerlo'''
def inversa(cadena):
    resul = ''
    for c in cadena:
        resul = c + resul
    return resul
