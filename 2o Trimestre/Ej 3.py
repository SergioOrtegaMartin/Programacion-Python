txt = '''hola hola hola hola adios adios adios pepe pepe pepe'''

diccionario = {}
for k in txt.split(' '):
    if k in diccionario:
        diccionario[k] += 1 

    else:
        diccionario[k] = 1
        
print (diccionario)
 