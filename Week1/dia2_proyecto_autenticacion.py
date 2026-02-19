#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PROYECTO DÍA 2: Sistema de Autenticación
Autor: Isaac Gutierrez
Fecha: 2025-02-16
Descripción: Simula un sistema de login con validaciones
"""
print("|´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´|")
print("|   SISTEMA DE AUTENTICACIÓN   |")
print("|______________________________|")
print()

# Disque base de datos ejemplo
usuarios = {
    "admin": "admin123",
    "isgeti": "geti123",
    "user1": "pass123"
}

intentos_maximos = 3
intentos = 0

print("Inicia Sesión")
print("-" * 40)

# Bucle de intentos
while intentos < intentos_maximos:
    usuario = input("Usuario: ")
    password = input("Contraseña: ")

# Verficar si el usuario existe
    if usuario in usuarios:
    # Verificar contraseña
        if usuarios[usuario] == password:
            print("\n" + "=" * 40)
            print("Login Exitoso")
            print("=" * 40)
            print(f"Bienvenido {usuario}")

            # Menú de opciones
            print("\n Opciones Disponibles: ")
            print("1. Ver Perfil")
            print("2. Cambiar Contraseña")
            print("3. Cerrar Sesión")

            opcion = input("Elige una opción (1-3): ")
            if opcion == "1":
                print(f"\n PERFIL DE {usuario.upper()}")
                print(f"Estado activo")
                print(f"Nivel de acceso: Usuario estándar")
            elif opcion == "2":
                nueva = input("Nueva contraseña: ")
                if len(nueva) >= 8:
                    usuarios[usuario] = nueva # Actualiza la contraseña
                    print("Contraseña Actualizada")
                else:
                    print("La contrseña debe tener al menos 8 caracteres")
            elif opcion == "3":
                print("Sesión Cerrada")
            else:
                print("Opción Inválida")

            break  # Salir del bucle while
        else:
            intentos += 1
            print(f"\n Contraseña incorrecta")
            print(f"Intentos restantes: {intentos_maximos - intentos}")
    else:
        intentos += 1
        print(f"\n Usuario no encontrado")
        print(f"Intentos restantes: {intentos_maximos - intentos}")
    
    print()

# Si agotó los intentos entonces
if intentos == intentos_maximos:
    print("\n ACCESO BLOQUEADO")
    print("Has excedido el número máximo de intentos")
    print("Contacta al admministrador del sistema")