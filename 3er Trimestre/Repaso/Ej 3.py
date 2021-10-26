'''3. Escribir en un fichero llamado secuencias.fasta la sguiente secuencia
>seq1
ACTG'''

f = open('secuencias.fasta', 'w+')

f.write('>seq1 \n ACTG')

f.close()