# Analiza texto letra por letra
# Isaac Gutierrez

texto = "PYTHON"

print("Letra por letra: ")
for letra in texto:
    print(letra)

#Contar vocales
print("=== CONTADOR DE VOCALES ===")
frase = input("Ingresa una Frase: " ).upper() 
vocales = 0

for letra in frase:
    if letra in "AEIOU":
        vocales += 1 

print(f"La frase tiene {vocales} vocales")