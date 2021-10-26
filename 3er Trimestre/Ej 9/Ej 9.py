'''Escribir una funcion a la que se le pasa como parametro un str que es el nombre del fichero
Esa funcion tiene que analizar el texto contenido en el fichero y devolver un objeto diccionario
Que tiene como clave cada palabra que detecte en el fichero y como valor el numero de veces que sale
La funcion controla (dispara y trata) posibles excepciones'''

def contar_palabras(fichero):
    'Con esta funcion pasamos un .txt a lista para después pasarlo a str y contar las palabras repetidas en un diccionario'
    try:
        f = open(fichero)
        listalineas = f.readlines()
        strtexto = ''.join(listalineas)
        palabras = strtexto.split()
        diccionario = {}

        for p in palabras:
            if p in diccionario:
                diccionario[p] += 1
            else:
                diccionario[p] = 1
        return diccionario
    except FileNotFoundError:
        print("Este fichero no existe")


resultado = contar_palabras('9.txt')
print(resultado)  # Para comprobar que está bien, lo imprimimos
# help(contar_palabras)
