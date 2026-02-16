#!/usr/bin/env python3
"""
DÍA 0: Verificación de Configuración
Autor: Isaac Gutierrez
Fecha: 2025-02-16
"""

import sys
import platform

print("╔════════════════════════════════════════╗")
print("║  CONFIGURACIÓN COMPLETADA ✅          ║")
print("╚════════════════════════════════════════╝")
print()
print(f"👤 Estudiante: Isaac Gutierrez")
print(f"🖥️  Sistema: {platform.system()} {platform.release()}")
print(f"🐍 Python: {sys.version.split()[0]}")
print(f"📂 Directorio: {sys.path[0]}")
print()

# Verificar librerías
librerias = ['requests', 'scapy', 'bs4', 'colorama', 'pandas', 'dns.resolver', 'whois']
print("📦 Librerías instaladas:")

for lib in librerias:
    try:
        __import__(lib)
        print(f"   ✅ {lib}")
    except ImportError:
        print(f"   ❌ {lib}")

print()
print("🎉 ¡Entorno listo para comenzar!")
print("🚀 Siguiente paso: Día 1 del plan de estudios")