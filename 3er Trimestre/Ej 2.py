while True:
    try:
        numero1=int(input("Introduce un número "))
        numero2=int(input("Introduce un número para dividir el anterior "))
        division= numero1/numero2
        print("El resultado de dividir el primer numero entre el segundo es " ,division)
    except (ZeroDivisionError, ValueError):
        print("No puedes introducir letras y el divisor no puede ser 0")