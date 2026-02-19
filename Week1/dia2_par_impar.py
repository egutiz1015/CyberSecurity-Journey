# Detector de número par o impar
# Autor: Isaac Gutierrez

print("=== DETECTOR PAR/IMPAR ===")
numero = int(input("Ingresa un número: "))

# El operador % (módulo) da el residuo de una división
# Si numero % 2 es 0, es par
# Si numero % 2 es 1, es impar
# 10 % 2 = 0 (10 dividido entre 2 = 5, residuo 0)
# 11 % 2 = 1 (11 dividido entre 2 = 5, residuo 1)
# 15 % 5 = 0 (15 dividido entre 5 = 3, residuo 0)

if numero % 2 == 0:
    print(f"{numero} es PAR")
else:
    print(f"{numero} es IMPAR") 