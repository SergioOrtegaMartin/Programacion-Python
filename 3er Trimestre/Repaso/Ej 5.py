'''5. Escribir los numeros del 1 al 100 en un fichero'''
f = open('Numeros.txt', 'w')

for i in range (1,101):
    f.write(str(i) + '\n')   
    
f.close()