#0 ¿Qué hace esta función?
def ej(n):
    print()
    print('Ejercicio', n, '_'*50)
    

#1 Escribe la salida que produce este código
print(9/2)          
print(str(9/2))     
print(9//2)         
print(-9//2)         
print(int(9/2))      
print(float(9//2))    
print(9%2)    
print(bool(9%2))      
print(9**2)    
print(9/0)

#2 Escribe la salida que produce este código

cadena = 'abcdefg'
print(cadena[0])      
print(cadena[-1])    
print(cadena[len(cadena)-1])    
print(cadena[2:4])    
print(cadena[:4])     
print(cadena[4:])     
print(cadena[:4] + cadena[4:])  
print (cadena[-6:-2])   
print(cadena [:])     
print(cadena[:10])    

# 3.Escribe la salida que produce este codigo
print(cadena[20])      
print(cadena[:20])      
print(cadena[len(cadena)])  
cadena[0]='X'     
cadena2='abcdefg'
print(cadena==cadena2, cadena is cadena2)  

#4. Escribe la salida que produce este codigo
cadena = 'abcdefg'
lista= list(cadena)
print(lista)   

lista.insert(2,'i')
print(lista)    

print(lista.index('c')) 

elemento=lista.pop(3)   
print(lista)    
print(elemento)  
print(type(elemento))   

lista.remove('d') 
print(lista)     

lista[0]='¡'    
lista[4:]='n'
lista.append('!')
print(lista)    

cadena=''
for car in lista:
    cadena +=car
print(cadena)     
    
trampa=lista.reverse()
print(trampa)  
    


#5 Escribe la salida que produce este codigo
a,b= 0,1

while b<10:
    print(b)
    a,b = b,a+b   
    
a='x'
b='x'
print(a==b) 
print(a is b)

a=['x']
b=['x']
print(a==b)
print(a is b) 


#6 ¿Qué hace el siguiente código?

while False:
    print('no')  
    
while True:
    print('si')  
  
si=True
no=False

while si or no:
    print(si,no)
    si, no = no, si  
  
si=True
no=False

while si and no:        
    print(si, no)
    si, no = no, si


#7 Escribe la salida que produce este codigo

t=1,10,3
print(type(t))   

a,b,c=t
print(a,b,c)

t[0]=1

lista=[1,2,3]

x=(lista,t)
print(x)

print(type(x))
print(type(x[0]))


#8 Escribe la salida que produce este codigo

a=x[0]
print(a)
print(type(a))

a[1]= 'x'     #Produce error? Por que?

print(a)
print(lista)
print(x)

#9. Escribe la funcion divisible(a,b) que devuelve un bool:
#True si a es divisible entre b, False en caso contrario



#Escribe un codigo de llamada a la funcion para que nos devuelve un true y un False



#10 Que hace la siguiente funcion?

def fun(lista):
    lista[0], lista[1:] = lista[len(lista)-1], lista[:len(lista)-1]
    
#Que devuelve esta funcion?
    
#Escribe la salida que produce este codigo

frase= ['es','la','caña','python']
fun(frase)
print(frase)

#11 Escribe la salida que produce este codigo
numeros='tres', 'dos','uno','cero',
print(type(numeros))
ordena=sorted(numeros)
print(ordena)
print(type(ordena))
print(numeros)
ordena.sort(key=len, reverse=True)
print(ordena)