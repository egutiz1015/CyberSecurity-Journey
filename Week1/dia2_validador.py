# Validadorque solo acpeta números positivos
# Autor: Isaac Gutierrez

print("=== VALIDADOR DE NÚMEROS ===")
entrada = input("Ingresa un número positivo: ")

if entrada.isdigit():                                             # Verficar si el texto son solo dígitos con isdigit()
    numero = int(entrada)

    if numero > 0:
        print(f"{numero} es un número positivo válido")            # Cuidar la estructura de los if-else para un buen funcionamiento
        print(f"su doble es: {numero * 2}")
        print(f"su mitad es: {numero / 2}")
    else:
        print("El número debe ser mayor a 0")
else:
    print("Eso no es un número válido")