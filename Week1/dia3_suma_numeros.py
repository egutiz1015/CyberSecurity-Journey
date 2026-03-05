# Sumador de números
# Autor: Isaac Gutierrez

print("=== SUMADOR DE NÚMEROS ===")
cantidad = int(input("¿Cuántos números quieres sumar? "))

suma_total = 0

for i in range(cantidad):
    numero = int(input(f"Número {i+1}: "))
    suma_total += numero  # Equivale a: suma_total = suma_total + numero

print(f"\nLa suma total es: {suma_total}")
print(f"El promedio es: {suma_total / cantidad}")