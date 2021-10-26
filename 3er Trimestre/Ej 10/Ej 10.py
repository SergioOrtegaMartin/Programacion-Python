modo = input('Si quieres añadir texto a un fichero, pulsa la tecla a, si quieres reemplazar el texto pulsa le tecla w \n')
fichero = input('Introduce el nombre del fichero \n')

def entrada_fichero(fichero,modo):
    f = open(fichero, modo)
    print('Creando fichero con nombre', fichero)
    print('Escribirás linea a linea hasta que introduzcas el caracter &')
    texto = input('Linea--->')
    while texto!= '&':
        f.write(texto)
        f.write('\n')
        texto = input('Linea--->')
    
    f.close()
    
try:
    entrada_fichero(fichero, modo)
    
except (ValueError):
    print('La letra w o la letra a deben ser minusculas')