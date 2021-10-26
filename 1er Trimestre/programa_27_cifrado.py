'''Desplazar en una cadena de caracteres cada caracter se desplaza uno

Ana = Cpc

funcion cifrar(cadena, clave)
devuelve la cadena cifrada desplzada con clave'''


def cifrar(cadena, clave):
    cifrada = ''
    for i in range(len(cadena)):
        c = cadena[i]
        nuevo_c = chr((ord(c) + clave))
        b = (ord(c) + clave)
        if (b > 90 and b < 97) or b > 122 :
            b = b - (90 - 64 + clave)
            cifrada = chr((b + clave)) 
        else:
            cifrada = cifrada + nuevo_c   
    return cifrada
     
entrada = input('Escribe algo: ')
print(cifrar(entrada, 2))

