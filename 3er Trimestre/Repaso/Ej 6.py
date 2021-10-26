'''6. Escribir en un fichero separado por tabuladores \t la informacion de un paciente almacenada en un diccionario
paciente = {'nombre':'Sergio', 'Edad' : '21'}

Pista. Podemos añadir todo lo que queramos escribir a una lista de cadenas de texto y después utilizar el metodo join'''

paciente = {'nombre':'Sergio', 'Edad' : '21', 'Diabetico':'False'}

lista=[]
for clave, valor in paciente.items(): 
    lista.append(valor)
    
StrLista = ' '.join(lista)
