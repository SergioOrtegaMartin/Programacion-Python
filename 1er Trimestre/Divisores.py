#Escribe una función que le pasamos un número y devuelve una tupla con los divisores de ese número.



print("Introduce el numero")
numero = int(input())
divisores=[]
for divisor in range(1,numero+1):
    if (numero % divisor) == 0 :
        divisores.append(divisor)        

tuple('divisores')


print(divisores)


     
