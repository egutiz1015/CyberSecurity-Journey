# Tabla de Multiplicar
# Isaac Gutierrez

print("=== TABLA DE MULTIPLICAR ===")
numero = int(input("¿De qué número quieres la tabla de Multiplicar? "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")