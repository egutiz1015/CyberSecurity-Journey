# Conversor Celsius a Fahrenheit
# Fórmula: F = C * 9/5 + 32
# Autor: Isaac Gutierrez

#título del conversor de temperatura
print("="*40)
print("== CONVERSOR DE TEMPERATURA ==")
print("== CELCIUS A FAHRENHEIT ==")
print("="*40)

#se pide la temperatura en celcius
celcius = input("Temperatura en Celcius: ")

#se hace la conversión de celcius a fahrenheit con la fórmula y se convierte en decimal
fahrenheit = float(celcius) * 9/5 + 32

#se muestra el resultado 
print(celcius + " grados Celcius son " + str(fahrenheit) + " grados Fahrenheit")