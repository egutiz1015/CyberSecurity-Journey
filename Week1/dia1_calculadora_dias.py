#Calculadora en días
#Autor: Isaac Gutierrez

print("== CALCULADORA DE EDAD EN DÍAS ==")
nombre = input("Tu nombre: ")
edad = input("Tu edad en años: ")

#convertir texto a número para poder multiplicarlo
edad_numero = int(edad)

#calcular días aprox 365 días por año
dias = edad_numero * 365

#mostrar resultado 

print("")
print("Hola " + nombre + "!")
print("Has vivido aproximadamente " + str(dias) + " días")