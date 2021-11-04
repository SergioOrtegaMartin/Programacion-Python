def balanza(lista):
    for i in range(1,len(lista)):
        if sum(lista[:i]) == sum(lista[i+1:]):
            return i
    
    return None

numeros = [9,2,4,1,1,2,1,0]
print("Posición central: ", balanza(numeros))