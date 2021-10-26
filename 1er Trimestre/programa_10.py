'''imprimir los caractereces de una cadena.
B. al reves'''


entrada = input('Escribe algo: ')

for i in range(len(entrada)):
    print(entrada[i])


entrada = input('Escribe algo: ')

for i in range(len(entrada)):
    print(entrada[len(entrada) -1 -i])

    

entrada = input('Escribe algo: ')

for i in range(len(entrada)-1,-1,-1):
    print(entrada[i])


entrada = input('Escribe algo: ')

for i in range(len(entrada)):
    print(entrada[-i - 1])
    
