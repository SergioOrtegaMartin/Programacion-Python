#Diccionario para crear los numeros de teléfono. Lo vamos a llamar telefono
#Crear programa que vaya leyendo por teclado nombres y numero de telefono y lo vaya añadiendo a un diccionario
#Hasta que le introduzcamos un asterisco
#b) Que saque un listado del diccionario

def captura():
    telefono = {}
    nombre=input("Nombre: ")

    while nombre!= '*':
        numero=input("Num Telefono: ")
        telefono[nombre]=numero
        nombre=input("Nombre: ")
        

    return(telefono)

def listar_contactos(telefono):
    for contacto in telefono:
        print(contacto,'--->', telefono[contacto])

print ("Los numeros son")
agenda=captura()
listar_contactos(agenda)

    
    


        



