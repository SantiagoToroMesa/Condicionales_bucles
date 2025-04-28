import random

def ejercicio5():
    numrandom = random.randint(1, 10)
    intentos = 3
    while intentos > 0:
        try:
            num = int(input("Adivina el numero entre 1 y 10: "))
            if num < 1 or num > 10:
                print("El numero debe estar entre 1 y 10")
                continue

            elif num > numrandom:
                print("El numero es menor")

            elif num < numrandom:
                print("El numero es mayor")

            if num == numrandom:
                print("¡Felicidades! Adivinaste el número.")
                break

            else:
                intentos -= 1
                if intentos > 0:
                    print(f"Incorrecto. Te quedan {intentos} intentos.")

                else:
                    print(f"Lo siento, has perdido. El número era {numrandom}.")

        except ValueError:
            print("ERROR INGRESA UN NUMERO ENTERO")
