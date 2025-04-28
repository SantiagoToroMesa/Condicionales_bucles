def ejercicio3():
    """
    Este programa solicita al usuario un número y muestra la tabla de multiplicar de ese número.
    """
    while True:
        try:
            numero_multi = int(input("Ingrese el numero a multiplicar: "))
            print(f"Tabla de multiplicar del numero {numero_multi}: ")
            for i in range(1,11):
                print(f"{numero_multi} x {i} = {numero_multi * i}")
            break

        except ValueError:
            print("ERROR INGRESA UN NUMERO ENTERO")