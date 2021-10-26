#Escribir una funcion que detecte si una nota está comprendida entre 0 y 10
#Si el usuario introduce una nota que no está comprendida entre 0 y 10 dispara la excepcion
#La funcion se llama LeeNota
#Si mete una letra en vez de un numero que vuelva a saltar la excepcion


def leenota():
    try:
        nota=int(input('Introduce tu nota: '))
        if  nota >10:
            print("La nota no puede ser mayor que 10 ")
        else:
            return nota
    except ValueError:
        print("No puedes introducir letras")
