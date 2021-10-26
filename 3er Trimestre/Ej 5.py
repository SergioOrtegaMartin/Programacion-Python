#Escribir una funcion que detecte si una nota está comprendida entre 0 y 10
#Si el usuario introduce una nota que no está comprendida entre 0 y 10 dispara la excepcion
#La funcion se llama LeeNota
#Si mete una letra en vez de un numero que vuelva a saltar la excepcion
#Escribir la funcion media5 que imprime la media de 5 notas introducidas


def lee_nota():
    '''Lee una nota que metamos por teclado y comprueba
    si está comprendida entre 0 y 10 y la devuelve.
    Dispara la excepcion ValueError en caso contrario
    o si el valor no es numérico'''
    
    nota=int(input('Introduce tu nota: '))
    if  nota < 0 or nota >10:
        raise ValueError
    
    return nota    

def media5():
    contador=0
    suma= 0
    while contador < 5:
        try: 
            nota = lee_nota()
            suma += nota
            contador += 1
            print(contador)
            
        except ValueError:
            print("No puedes introducir letras ni un numero no comprendido entre 0 y 10")
            
    return (suma/5)
        

