def entrada():
    lista = []
    nombre= input('dime el nombre del alumno:')
    while nombre != '*':
        nota1 = float(input('dime la nota de programacion:'))
        nota2 = float(input('dime la nota de entornos de desarrollo:'))
        nota3 = float(input('dime la nota de bases de datos:'))
        tupla_notas = (nota1,nota2,nota3)
        tupla_alumno = [nombre,tupla_notas]
        lista.append(tupla_alumno)

        nombre= input('dime el nombre del alumno:')
    
    return lista


def media_alumnos(alumnos):
    media = []
    for i in alumnos:
        tupla_nombre_notas = (i[0], (i[1][0] + i[1][1] + i[1][2])/3)
        media.append(tupla_nombre_notas)
            
    return media

def media_asignaturas(asignaturas):
    media1 = []
    tupla_asignaturas_notas = 0
    for i in asignaturas:
        tupla_asignaturas_notas += i[1][0]
    media1.append(tupla_asignaturas_notas)
        
    return media1

print(media_asignaturas(entrada()))