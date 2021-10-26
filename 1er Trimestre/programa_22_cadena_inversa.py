'''Escribir una funcion que se la pasa una cadena
y se le pasa la cadena inversa'''


def inversa(cadena):
    resul = ''
    for i in range (len(cadena)):
        resul = cadena[i] + resul
    return resul


print(inversa('Hola don Pepito, hola don Jose'))
