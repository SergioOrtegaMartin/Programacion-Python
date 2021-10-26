'''Coger un texto y contar cuántas palabras aparecen en un texto, la clave es la
palabra, y el valor el número de veces aparece'''

texto = '''La pálida es un término que se refiere a la situación donde una 
 persona se siente mal después de fumar marihuana. Las personas pueden ponerse 
 pálidas y sudorosas, sentirse mareados, con náuseas, incluso pueden empezar a 
 vomitar. Usualmente pueden sentir que necesitan acostarse de inmediato.'''

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




'''Que lo ordene por frecuencia '''

def segundo_valor(tupla):
    return tupla[1]

def ordena_cuenta(texto):
    texto_contado = cuenta_palabras(texto)
    return sorted(list(texto_contado.items()), key = segundo_valor, reverse = True)


    




 

    
               
    
    

    
