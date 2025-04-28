def ejercicio1():
    """
    Este programa solicita al usuario un número entero y determina si es positivo, negativo o cero.
    Si el usuario ingresa un valor no válido, se le pide que ingrese un número entero nuevamente.
    """
    while True:
        try:
            numero = int(input("Ingrese un numero entero: "))

            if numero > 0:
                print(f"el numero {numero} es positivo")
                break

            elif numero < 0:
                print(f"el numero {numero} es negativo ")
                break

            elif numero == 0:
                print("el numero es 0")
                break

        except ValueError:
            print("ERROR INGRESA UN NUMERO ENTERO")
