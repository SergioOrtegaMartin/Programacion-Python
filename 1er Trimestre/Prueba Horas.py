#Leer desde teclado unos intervalos de tiempo.
#Cada intervalo va a tener hora/min/seg
#Caputuramos cada intervalo y lo guardamos en una tupla que guardaremos dentro de una lista hasta que pongamos un asterisco
#Calcular la suma total de todos los intervalos y devolver el final en 3 valores
#apartado a.1) crear una función que reduzca las cantidades de la tupla al formato
#apartado b) Hacer lo mismo pero con dias/horas/min/seg

#def capturartiempos
listatiempos=[]
tuplatiempos=()
horas=int(input("Horas\n"))
while horas != -1:
    minutos=int(input("Minutos \n"))
    segundos=int(input("Segundos\n"))
    tuplatiempos=(horas, minutos, segundos)
    listatiempos.append(tuplatiempos)
    print("Para dejar de añadir valores, en horas pon '-1'")
    horas=int(input("Horas\n"))

print (listatiempos)
