
#def captura_datos()

contacto=[]
nombre=input("introduce el nombre:")
while nombre!= '*':
    contacto.append(nombre)
    contacto.append(input("introduce el correo: "))
    contacto.append(input("introduce el movil: "))
    contacto.append(input("introduce el telefono fijo: "))
    list(contacto)


diccionario= {}

diccionario[contacto[0]]=contacto

print (diccionario)