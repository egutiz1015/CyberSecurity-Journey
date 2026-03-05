# Validación de entrada de edad
# Autor: Isaac Gutierrez

print("=== INGRESO DE EDAD ===")

while True:
    edad = input("Ingresa tu edad (0-120): ")

    if edad.isdigit():
        edad = int(edad)

        #Verificar rango válido
        if 0 <= edad <= 120:
            print("Edad válida :)")
            print(f"Tu edad es: {edad}")
            break
        else:
            print("!La edad debe estar entre 0-120!")

    else:
        print("Debes ingresar una número")