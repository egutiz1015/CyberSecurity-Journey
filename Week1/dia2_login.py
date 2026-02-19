# Sistema de Login básico
# Autor: Isaac Gutierrez

print("=== SISTEMA DE LOGIN ===")

# Dos variables que almacenan el usuario y password correctos
usuario_correcto = "geti"
password_correcto = "12345"   # Nunca guardar contraseñas en un código, esto es solo didáctico

# Se solicita el usario y contraseña 
usuario = input("Ingrese el usuario: ")
password = input("Ingrese la contraseña: ")

# Si el usuario y password son los correctos hacer login de lo contrario no con un condicional
if usuario == usuario_correcto and password == password_correcto:
    print("\n Login exitoso")
    print("Bienvenido al sistema")
else:
    print("Usuario o contraseña incorrectos")
    print("Acceso denegado")