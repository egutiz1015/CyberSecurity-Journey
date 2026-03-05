# Generador de contraseñas simple
# Autor: Isaac Gutierrez

import random
import string

print("=== GENERADOR DE CONTRASEÑAS ===")
longitud = int(input("Longitud de la contraseña (8-32): "))

# Caracteres disponibles
caracteres = string.ascii_letters + string.digits + "!@#$%"

password = ""
for i in range(longitud):
    password += random.choice(caracteres)

print(f"\n Tu contraseña: {password}")