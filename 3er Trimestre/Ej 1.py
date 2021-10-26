

'''Captura de notas por alumnos'''

numero_modulos = int(input('¿Cuántos módulos dais? '))
numero_alumnos = int(input('¿Cuántos alumnos hay en clase? '))

def entrada_notas ():
    lista_total = []
    for i in range (numero_alumnos):
        lista_alumno = []
        for j in range(numero_modulos):
            nota = float(input('Introduce la nota: '))
##        nota_0 = float (input ('Nota en primer mnódulo: '))
##        nota_1 = float (input ('Nota en segundo módulo: '))
##        nota_2 = float (input ('Nota en tercer módulo: '))
##        nota_3 = float (input ('Nota en cuarto módulo: '))
##        nota_4 = float (input ('Nota en quinto módulo: '))
            lista_alumno.append(nota)
        print()
        lista_total.append(lista_alumno)

    return lista_total


'''Media de cada alumno'''

def media_alumno (lista):
    lista_media = []
    for e in lista:
        media = sum(e) / numero_modulos
        lista_media.append(media)

    return lista_media


def media_alumno_ordenada(lista):
    lista_notas = media_alumno(lista)
    lista_ordenada = sorted(lista_notas, reverse = True)
    return lista_ordenada
        
'''Media de módulo'''

def media_modulo (lista):
    lista_media = []
    for i in range (numero_modulos):
        num = 0
        for j in range (numero_alumnos):
            num += lista[j][i]
        nota_media_modulo = num / numero_alumnos
        lista_media.append(nota_media_modulo)

    return lista_media
            
