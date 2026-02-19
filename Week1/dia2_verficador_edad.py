# Verficador de edad
# Autor: Isaac Gutierrez

print("==VERFIFICADOR DE EDADES==")
edad = int(input("¿Qué edad tienes? "))

if edad >= 18:
    print("Eres mayor de edad")
    print("Puedes votar y obtener licencia de conducir")
else:
    print("Eres menor de edad")
    edad_faltante = 18 - edad
    print(f"Te faltan {edad_faltante} años para ser mayor de edad")