# Juego: Adivina el número
# Autor: Isaac Gutierrez

import random

print("=== JUEGO: ADIVINA EL NÚMERO ===")
numero_secreto = random.randint(1, 100)
intentos = 0
maximo_intentos = 7

print("He pensado un número entre 1 y 100")
print(f"Tienes {maximo_intentos} intentos\n")

while intentos < maximo_intentos:
    intento = int(input("¿Qué número es? "))
    intentos += 1
    
    if intento == numero_secreto:
        print(f"\n🎉 ¡CORRECTO! Lo adivinaste en {intentos} intentos")
        break
    elif intento < numero_secreto:
        print("⬆️  El número es MAYOR")
    else:
        print("⬇️  El número es MENOR")
    
    print(f"Intentos restantes: {maximo_intentos - intentos}\n")

if intentos == maximo_intentos and intento != numero_secreto:
    print(f"\n Perdiste. El número era: {numero_secreto}")