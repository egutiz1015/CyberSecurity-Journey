# Buscador de números primos
# Autor: Isaac Gutierrez

print("=== BUSCADOR DE NÚMEROS PRIMOS === ")
limite = int(input("Buscar números primos hasta: "))

print(f"\nNúmeros primos del 2 hasta el {limite}: ")
contador_primos = 0

for num in range(2, limite + 1):
    es_primo = True

    #Verificador si es divisible por algún número 
    for divisor in range(2, num):
        if num % divisor == 0:
            es_primo = False
            break                 # Si encontró divisor ya no es primo
    
    if es_primo:
        print(num, end="")
        contador_primos += 1

print(f"\n\nTotal de primos encontrados: {contador_primos}")