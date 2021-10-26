'''Añadir al fichero anterior la secuencia:
>seq2
GATA   '''

f = open('secuencias.fasta', 'a+')

f.write('\n>seq2 \n GATA')

f.close()