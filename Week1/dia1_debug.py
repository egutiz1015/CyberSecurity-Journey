# Programa con errores (NO FUNCIONA)

print("Calculadora simple")  # Error 1: ¿Qué falta? falta cerrar comillas

numero1 = input("Primer número: ")
numero2 = input("Segundo número: ")

#variante de Claude más optimizada

#suma = int(numero1) + int(numero2)

n1 = int(numero1)
n2 = int(numero2)

suma = n1 + n2  # Error 2: ¿Qué tipo de datos suma? texto, asi que en lineas 8-9 los convertí en enteros int para operarlos

print("La suma es: " + str(suma))  # Error 3: ¿Puedes sumar texto directamente? como se convirtieron a int ahora se regresa a str para poder concatenarlo y no sumarlo como operación