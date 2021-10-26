'''a)Hacer un ejercicio donde se crea una agenda en formato csv 
Para ello el usuario introduce 3 valores (nombre, tel, email) hasta que el nombre sea una cadena vacia 
Esta función debe ser un archivo csv que guardaremos como ‘agenda.csv’'''

'''b)crear otra funcion (carga)que le paso el nombre de la agenda y me la carga en un diccionario
que tiene como clave el nombre y como valor el registro completo como una tupla
por ejemplo:
{pepe: ('pepe', 44, 622367745)}'''

'''c) Una tercera funcion permite consultar de forma interactiva el telefono y el mail
pide nombre y devuelve telefono y mail
BUCLE'''

'''Controlar como excepciones que el fichero no exista, que en el fichero exista un formato diferente al que tenemos
(Que haya mas de 3 valores), y en la lectura verificar que el contacto exista(contacto error)'''


modo = input('Si quieres añadir texto a un fichero, pulsa la tecla a, si quieres reemplazar el contenido pulsa le tecla w \n')
fichero = input('Introduce el nombre del fichero \n')

def agenda(fichero,modo):
    try:
        f = open(fichero + '.csv', modo)
        print('Agenda creada con el nombre --->', fichero)
        print('Escribirás linea a linea hasta que introduzcas el nombre vacio')
        #f.write('Nombre, telefono, email')
        #f.write('\n')
        nombre = input('Introduce el nombre: \n')
        while nombre!= '':
            f.write(nombre + ',')
            telefono = input('Introduce el telefono: \n')
            f.write(telefono + ',')
            email = input('Introduce el email:  \n' )
            f.write(email + ',')
            f.write('\n')
            nombre = input('Introduce el nombre: \n')
    except(PermissionError):
        print('No tienes permisos para abrir el archivo, prueba a cerrarlo si lo tienes abierto con otro programa')
        
agenda(fichero,modo)  
        

'''b)crear otra funcion (carga)que le paso el nombre de la agenda y me la cargue en un diccionario
que tiene como clave el nombre y como valor el registro completo como una tupla
por ejemplo:
{pepe: ('pepe', 44, 622367745)}'''

def carga(fichero):
    try:
        lista=[]
        diccionario={}
        f = open(fichero)
        lineas = [linea.split(',') for linea in f]
        for linea in lineas:
            linea.pop()
            diccionario[linea[0]]=tuple(linea)
        print(diccionario)

    except FileNotFoundError:
        print("Este fichero no existe")
    





        
        
        
      