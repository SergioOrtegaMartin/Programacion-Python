''' tabla de multiplicar de un numero
7 x 0 = 0'''


entrada = int(input('Introduce un número: ' ))

for i in range(11):
    print(entrada,'x',i,'=',entrada*i)


    
entrada = int(input('Introduce un número: ' ))
valores = int(input('Introduce el tamaño: '))

for i in range(valores + 1):
    print(entrada,'x',i,'=',entrada*i)
