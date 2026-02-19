# Calculadora de calificaciones
# Autor: Isaac Gutierrez

print("===SISTEMA DE CALIFICACIONES===")
nota = float(input("Ingresa tu calificación (0-100): "))

if nota > 90:
    print("¡Excelente nota! :D ")
elif nota >= 80:
    print("¡Muy bien! :) ")
elif  nota >= 70:
    print("¡Bien! c: ")
elif nota >= 60:
    print("Suficiente :/ ")
else:
    print("Reprobado .C ")
    print("¡Necesitas estudiar más!")

if nota >= 60:
    print("\nC: !Aprobaste el curso!")
else:
    print("\n:C No aprobaste, pero puedes mejorar... ")