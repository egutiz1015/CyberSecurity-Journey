#!/usr/bin/env python3
"""
PROYECTO DÍA 3: Escáner de Puertos Básico (Simulado)
Autor: Isaac Gutierrez
Descripción: Simula un escáner que verifica puertos comunes
"""

import random
import time

print("╔════════════════════════════════════════╗")
print("║      PORT SCANNER SIMULATOR v1.0       ║")
print("╚════════════════════════════════════════╝")
print()

# Puertos comunes y sus servicios
puertos_comunes = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    5432: "PostgreSQL",
    8080: "HTTP-Alt",
    3389: "RDP"
}

target = input(" IP objetivo (ej: 192.168.1.1): ")
print(f"\n Escaneando {target}...")
print("="*50)

puertos_abiertos = []
puertos_cerrados = []

# Simular escaneo
for puerto, servicio in puertos_comunes.items():
    print(f"Escaneando puerto {puerto} ({servicio})...", end=" ")
    time.sleep(0.3)  # Simula tiempo de escaneo
    
    # Simular aleatoriamente si está abierto o cerrado
    # 33% chance de estar abierto
    if random.choice([True, False, False]):
        print(" ABIERTO")
        puertos_abiertos.append((puerto, servicio))
    else:
        print(" CERRADO")
        puertos_cerrados.append((puerto, servicio))

# Generar reporte
print("\n" + "="*50)
print(" REPORTE DE ESCANEO")
print("="*50)
print(f"Objetivo: {target}")
print(f"Puertos escaneados: {len(puertos_comunes)}")
print(f"Puertos abiertos: {len(puertos_abiertos)}")
print(f"Puertos cerrados: {len(puertos_cerrados)}")

if puertos_abiertos:
    print("\n PUERTOS ABIERTOS:")
    for puerto, servicio in puertos_abiertos:
        print(f"  • Puerto {puerto} - {servicio}")
        
        # Advertencias de seguridad
        if puerto == 23:
            print("ALERTA: Telnet no es seguro, usa SSH")
        elif puerto == 21:
            print(" ADVERTENCIA: FTP transmite en texto plano")
        elif puerto == 3389:
            print(" INFO: RDP debe estar protegido")

print("\n ¿Guardar reporte? (s/n): ", end="")
if input().lower() == "s":
    filename = f"scan_{target.replace('.', '_')}.txt"
    
    with open(filename, "w") as f:
        f.write(f"REPORTE DE ESCANEO\n")
        f.write(f"{"="*50}\n")
        f.write(f"Objetivo: {target}\n")
        f.write(f"Fecha: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("PUERTOS ABIERTOS:\n")
        for puerto, servicio in puertos_abiertos:
            f.write(f"  {puerto} - {servicio}\n")
        
        f.write(f"\nPUERTOS CERRADOS:\n")
        for puerto, servicio in puertos_cerrados:
            f.write(f"  {puerto} - {servicio}\n")
    
    print(f" Reporte guardado en: {filename}")
else:
    print("Reporte no guardado.")

print("\n Escaneo completado")