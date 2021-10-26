#4.2 Borrar lo añadido

f = open('secuencias.fasta', 'r+')
line = f.readline()
f.seek(3,0)
f.write('Hola')5.
f.close()