from ejercicio1 import ejercicio1
from ejercicio2 import ejercicio2
from ejercicio3 import ejercicio3
from ejercicio4 import ejercicio4
from ejercicio5 import ejercicio5

""""Menu principal donde ingresaremos el numero del ejercicio que deseemos ejecutar"""

def menu():
    print("""Ingrese el numero del ejercicio que desea ejecutar:
    ============================================================
    1. Clasificado de numeros (Ejercicio 1)
    2. Validación de calificaciones (Ejercicio 2)
    3. Tabla de multiplicar (Ejercicio 3)
    4. Contador regresivo (Ejercicio 4)
    5. Adivinador de numero (Ejercicio 5)
    6. Salir""")
    opcion = input("Selecione una opcion: ")
    return opcion

while True:
    opcion = menu()

    if opcion == "1":
        ejercicio1()

    elif opcion == "2":
        ejercicio2()

    elif opcion == "3":
        ejercicio3()

    elif opcion == "4":
        ejercicio4()

    elif opcion == "5":
        ejercicio5()

    elif opcion == "6":
        print("Saliendo del programa...")
        break

    else:
        print("Debes ingresar un numero del 1 al 6")