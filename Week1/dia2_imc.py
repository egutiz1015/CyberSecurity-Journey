# Calculadora de Índice de masa Corporal (IMC)
# Autor: Isaac Gutierrez

print("=== CALCULADORA DE IMC ===")
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros (ej. 1.75): )"))

# Calcular IMC: peso / altura^2
imc = peso / (altura ** 2)

print(f"Tu IMC es {imc:.2f}")    # .2f muestra solo 2 decimales

# Clasificación según la OMS
if imc < 18.5:
    print("Clasificación: Bajo Peso")
elif imc < 25:
    print("Clasificación: Peso Normal")
elif imc < 30:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificación: Obesidad")

# Recomendación
if imc < 18.5 and imc < 25:
    print("¡Tu peso está en el rango saludable!")
else:
    print("¡Consulta con un profesional sobre tu salud!")