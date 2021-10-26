''' escribir un programa que pida un texto al usuario  escriba letra a letra
todo los caracteres del texto'''


entrada = input('Escribe un texto: ')
cadena = entrada
contador = 0
while contador < len(cadena):
    print(cadena[contador])
    contador = contador + 1
    

