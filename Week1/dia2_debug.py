# Este programa tiene errores. Encuéntralos y corrígelos.

print("=== VERIFICADOR DE CONTRASEÑA ===")
password = input("Crea una contraseña: ")

# Verificar longitud
if len(password) < 8:
    print("❌ La contraseña debe tener al menos 8 caracteres")
else:
    print("✅ Longitud adecuada")

# Verificar si tiene números
tiene_numero = False
for caracter in password:
    if caracter.isdigit():
        tiene_numero = True

if tiene_numero == True:
    print("✅ Contiene números")
else:
    print("❌ Debe contener al menos un número")