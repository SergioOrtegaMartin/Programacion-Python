#Funcion para cargar elementos a una lista a partir de una entrada de teclado de numeros hasta que se introduzca un 0
#Otra función que sume los elementos de esa lista
#Otra funcion que nos diga el número máximo y el número minimo de esa lista

intro = int
listanumeros=[]
    
while intro != 0:
    intro = int(input())
    listanumeros.append(intro)
    
listanumeros.pop()    
print ("Los numeros que has introducido son ", listanumeros)


sumalista= sum(listanumeros)
minlista= min(listanumeros)
maxlista= max(listanumeros)
print ("La suma de los numeros de la lista es ", sumalista, ", el numero mas pequeño introducido es ", minlista, "y el mayor es " ,maxlista)
