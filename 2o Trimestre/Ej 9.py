'''Escribir la funcion cuenta() a la que yo le paso un diccionario y un texto --cuenta(contador, texto)--'''

texto=input('Mete un texto: ')

palabras = texto.split(' ')
cuenta = {}
for e in palabras:
    if e in cuenta:
        cuenta[e] += 1 
    else:
        cuenta [e] = 1


'''Cuenta palabras con forma de función'''

def cuenta_palabras (texto):
    palabras = texto.split(' ')
    cuenta = {}
    for e in palabras:
        if e in cuenta:
            cuenta[e] += 1
        else:
            cuenta [e] = 1

    return cuenta


    
