'''Decir si un numero es primo o no'''


def es_primo(n):
    for i in range(2, n // 2 + 1):
        return n % i != 0
    return True


    
numero = int(input('Dime un numero y te digo si es primo: '))
print(es_primo(numero))


''' funcion a la que le pasamos un numero y esta funcion imprime todos los
numeros primos menores que ese numero'''

print()


def primo_hasta(limite):
    for i in range(1, limite):
        if es_primo(i):
            print(i)
    


numero_2 = int(input('Pon un numero y te digo los primos menores: '))
primo_hasta(numero_2)
        

            
            
            


''' funcion procidemental que imprima los n primeros primos'''


def n_primos(limite):
    for i in range(1, limite + 1):
        print(es_primo(i))
    return i

    
    
numero_2 = int(input('Pon un numero y te los n primos: '))
print(n_primos(numero_2))
        
    
