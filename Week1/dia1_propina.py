# Calculadora de propina para restaurante
# Autor: Isaac Gutierrez

print("=== CALCULADORA DE PROPINA ===")
total_cuenta = input("Total de la cuenta: $")
porcentaje = input("Porcentaje de propina (10, 15, 20): ")

# Convertir a números decimales
cuenta = float(total_cuenta)
porcentaje_num = float(porcentaje)

# Calcular propina
propina = cuenta * (porcentaje_num / 100)
total_pagar = cuenta + propina

# Mostrar resultados
print("\n--- RESUMEN ---")
print("Cuenta: $" + str(cuenta))
print("Propina (" + str(porcentaje_num) + "%): $" + str(propina))
print("TOTAL A PAGAR: $" + str(total_pagar))