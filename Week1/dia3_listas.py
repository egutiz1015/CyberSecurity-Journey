# Introducción a las listas
# Autor: Isaac Gutierrez

frutas = ["banano", "fresa", "mango", "naranja"]

print("Mis frutas favoritas son:")
for fruta in frutas:
    print(f"{fruta}")

# Con índice de numeración
print("\n=== LISTA NUMERADA ===")
for i in range(len(frutas)):
    print(f"{i+1}. {frutas[i]}")