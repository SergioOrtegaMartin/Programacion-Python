'''Escribir un programa que lea una serie indefinida de numeros hasta que
se introduzca un 0
el programa tiene que contar cuantos numeros hay entre 0 y 500 incluido,
500 y 1000
mayores que 1000 y menores que 0

el programa al final imprime los resultados'''


contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0

x = int(input('Escribe un número: '))
while x != 0:
    if x < 0:
        contador1 = contador1 + 1
        
    elif 0 < x <= 500:
        contador2 = contador2 + 1
        
    elif 500 < x <= 1000:
        contador3 = 1 + contador3
        
    else:
        contador4 = 1 + contador4
        
    x = float(input('Escribe un número: '))

print('Menores que 0:',contador1)
print('Entre 0 y 500:',contador2)
print('Entre 500 y 1000: ',contador3)
print('Mayores: 1000: ',contador4)



    


    
