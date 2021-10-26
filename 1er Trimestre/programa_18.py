'''Escribir la tabla de multiplicar de un numero y con cuantos elementos'''


def imprime_tabla(tabla, limite):
    for i in range(0, limite + 1):
        print(tabla, 'x', i,'=',tabla*i)





numero = int(input('escribe el numero y te hago la tabla: ' ))
cuantos = int(input('escribe hasta que numero lo quieres ' ))

imprime_tabla(numero, cuantos)
imprime_tabla(5, 10)




