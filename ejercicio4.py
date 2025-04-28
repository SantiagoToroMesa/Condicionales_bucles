def ejercicio4():

    """"ciclo desde un numero que ingrese el usuario hasta el cero"""

    while True:
        try:
            numwhile = int(input("Ingrese un numero entero: "))
            if numwhile < 0:
                print("Porfavor ingrese un numero positivo")
                return

            while numwhile > 0:
                print(numwhile)
                numwhile -= 1
            print("El ciclo ha terminado")
            break

        except ValueError:
            print("ERROR INGRESA UN NUMERO ENTERO")
