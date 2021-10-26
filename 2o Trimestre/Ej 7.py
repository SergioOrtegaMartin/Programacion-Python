'''1 Coger todas las palabras que haya en dos textos grandes y ver las palabras que estan en un texto y en otro
Split
2 Todas las palabras que están en el primer texto y no están en el segundo
Ordenar el resultado alfabéticamente
3 El conjunto de las letras distintas que forman parte de las palabras del ejercicio 1'''

#Ver palabras que estan en un texto y en otro
texto1='En cuanto a su autonomía y en el mejor de los casos, según ciclo WLTP, el BMW 32 Por su parte, el BMW 520e queda entre 53 y 61 kilómetros si hablamos del Sedán y entre 52 y 57 kilómetros cuando nos referimos al Touring.'
texto2='ofrece 663 kilómetros de autonomía, una aceleración de 0 a 100 km/h en 3,2 segundos y 250 km/h de velocidad punta. Por encima, el paquete Plaid apuesta por la aceleración bruta, con 1.020 CV de potencia y una aceleración de hasta 320 km/h, capaz de cubrir el 0 a 100 km/h en 2,1 segundos. Su autonomía es de 628 kilómetros. Por último, el paquete Plaid+ mantiene estas cifras de aceleración (incluso prometen bajar de 2,1 segundos) y, además, asegura una autonomía de más de 840 kilómetros.'

t1=texto1.split()
t2=texto2.split()

t1set=set(t1)
t2set=set(t2)
p_comun=t1set.intersection(t2set)
print('Las palabras en comun son: ')
print(p_comun)

#Palabras en el primer texto y no en el segundo
print('')
print('Las palabras que aparecen en el primer texto y no en el segundo son: ')
p_diferentes=t1set.difference(t2set)
print(p_diferentes)
print('')
print('Ordenadas alfabeticamente')
orden=sorted(p_diferentes)
print(orden)

#3
print('')
lista3=list(p_comun)
cadena = "".join(lista3)
b=set(cadena)
print('Las letras necesarias son')
print(b)

print('')
print('')

p_comun_lista = list(p_comun)
acumulador = ''
for letra in p_comun_lista:
    acumulador += letra
    
print(acumulador)
    
letras_set = set(acumulador)

    
    
    
    
    
