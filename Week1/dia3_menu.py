# Menú interactivo
# Autor: Isaac Gutierrez
import datetime

print("=== MENU PRINCIPAL ===")

while True:           # bucle infinito
    print("\n1. Saludar")
    print("2. Ver Hora")
    print("3. Calculadora Simple")
    print("4. Salir")

    opcion = input("\nSeleccione la opción que quiera: ")

    if opcion == "1":
        nombre = input("¿Tu nombre? ")
        print(f"¡Hola {nombre}!")
    elif opcion == "2":
        print(f"Hora actual: {datetime.datetime.now()}")
    elif opcion == "3":
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))
        print(f"Suma: {a + b}")
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else: 
        print("Opción Inválida")