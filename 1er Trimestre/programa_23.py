''' verificar si la nota es correcta si esta comprendida entre 0 y 10
si no no es valida'''



def lee_nota():
    '''Lee de teclado y devuelve el numero'''
    x = float(input('Pon una nota: '))
    if  0 <= x <= 10 :
        return x


print(lee_nota())
