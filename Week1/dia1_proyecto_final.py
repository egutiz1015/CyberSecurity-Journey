#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PROYECTO DÍA 1: Perfil de Hacker Ético
Autor: Isaac Gutierrez
Fecha: 2025-02-16
Descripción: Recopila información básica para crear un perfil
"""

print("╔════════════════════════════════════════╗")
print("║  CREADOR DE PERFIL - HACKER ÉTICO     ║")
print("╚════════════════════════════════════════╝")
print()

# Recopilar información
nombre = input("👤 Nombre completo: ")
edad = input("🎂 Edad: ")
pais = input("🌍 País: ")
lenguaje_actual = input("💻 ¿Sabes algún lenguaje de programación? (Sí/No): ")
objetivo = input("🎯 ¿Por qué quieres aprender ciberseguridad?: ")

# Calcular datos
dias_vividos = int(edad) * 365
horas_estudio = 5  # Horas diarias de estudio
dias_plan = 180    # 6 meses
horas_totales = horas_estudio * dias_plan

# Generar perfil
print("\n" + "="*50)
print("📋 TU PERFIL DE HACKER ÉTICO")
print("="*50)
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años ({dias_vividos} días de vida)")
print(f"País: {pais}")
print(f"Experiencia previa: {lenguaje_actual}")
print(f"Motivación: {objetivo}")
print()
print("📊 PLAN DE ESTUDIO")
print("-" * 50)
print(f"Horas de estudio diarias: {horas_estudio}")
print(f"Duración del plan: {dias_plan} días (6 meses)")
print(f"Total de horas de práctica: {horas_totales} horas")
print()
print("🎓 Al completar este plan, habrás invertido")
print(f"   {horas_totales} horas en convertirte en profesional")
print("="*50)

# Guardar en archivo
with open("Week1/mi_perfil.txt", "w", encoding="utf-8") as archivo:
    archivo.write("PERFIL DE HACKER ÉTICO\n")
    archivo.write("="*50 + "\n")
    archivo.write(f"Nombre: {nombre}\n")
    archivo.write(f"Edad: {edad}\n")
    archivo.write(f"País: {pais}\n")
    archivo.write(f"Objetivo: {objetivo}\n")

print("\n✅ Perfil guardado en 'Week1/mi_perfil.txt'")