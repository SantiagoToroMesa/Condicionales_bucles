def ejercicio2():
    """
    Este programa solicita al usuario que ingrese una nota entre 0 y 100.
    Si la nota es menor a 60, se imprime un mensaje indicando que ha reprobado.
    Si la nota es mayor o igual a 60, se imprime un mensaje indicando que ha aprobado.
    El programa sigue pidiendo la nota hasta que se ingrese un valor válido.
    """
    while True:
        try:
            nota = int(input("Ingrese una nota (0 - 100): "))
            if nota >= 0 and nota < 60 :
                print(f"Haz reprobado con una nota de {nota}")
                break
            elif nota >= 60 and nota <= 100:
                print(f"Haz aprobado con una nota de {nota}")
                break
            else:
                print("Ingrese un numero entre 0 - 100")
        except ValueError:
            print("¡INGRESE UN NUMERO ENTERO!")
