'''Escribe las 10 tablas de multiplicar'''

'''for tabla in range(11):
    print()
    for i in range(11):
        print(tabla, 'x',i ,'=', tabla*i)'''



'''que te diga de que numero hasta que numero
y cuantas veces lo quiere'''

entrada = int(input('el número que empieza la tabla: ' ))
veces = int(input('hasta que numero lo quiers: ' ))
multiplo = int(input('el multiplo: ' ))

        
for tabla in range(veces + 1):
    print()
    for i in range(multiplo + 1):
        print(entrada, 'x',i ,'=', entrada*i)
