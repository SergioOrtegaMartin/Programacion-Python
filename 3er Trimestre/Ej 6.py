#Escribir una funcion que detecte si una nota está comprendida entre 0 y 10
#Si el usuario introduce una nota que no está comprendida entre 0 y 10 dispara la excepcion
#La funcion se llama LeeNota
#Si mete una letra en vez de un numero que vuelva a saltar la excepcion
#Escribir la funcion media5 que imprime la media de 5 notas introducidas

class NotaFueraRango(Exception):
    pass
    

def lee_nota():
    '''Lee una nota que metamos por teclado y comprueba
    si está comprendida entre 0 y 10 y la devuelve.
    Dispara la excepcion ValueError si no es un valor numerico
    y dispara NotaFueraRango si no está comprendida entre 0 y 10'''
    
    nota=int(input('Introduce tu nota: '))
    if  nota < 0 or nota >10:
        raise NotaFueraRango
    
    return nota    

def media5():
    contador_entradas = 0
    contador = 0
    suma = 0
    while contador < 5:
        try: 
            nota = lee_nota()      
        except Exception:
            pass
        except ValueError:
            print("No puedes introducir letras")
        except NotaFueraRango:
            print('No puedes poner numeros no comprendidos entre 0 y 10')
        else:
            suma += nota
            contador += 1
            print('Llevas introducidas ',contador, 'notas correctas')
            
        finally:
            contador_entradas += 1 
    print('Has hecho', contador_entradas, 'entradas')       
    return (suma/5)
        





