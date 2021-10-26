'''Escribe un programa que nos pida a que potencia queremos y el limite
de que a cuantos numeros lo queremos'''



def elevado(x,y):
    return x ** y


def lee_entero(texto):
    '''captura y convertir a int entrada'''
    x = int(input(texto))
    return x

potencia = lee_entero('Dime el exponente de la potencia: ')
limite = lee_entero('Dime hasta que numero lo quieres: ')


for i in range(1, limite + 1):
    print(i, 'elevado', potencia, elevado(i,potencia))
          
    
