# Sistema de Descuentos en Tienda
# Autor: Isaac Gutierrez

print("=== SISTEMA DE DESCUENTOS ===")
precio = float(input("Precio del Producto: Q"))
es_cliente_vip = input("¿Eres cliente VIP? (si/no): ").lower()
cantidad = int(input("Cantidad de productos: "))

# Calcular subtotal
subtotal = precio * cantidad

# Aplicar descuentos
descuento = 0

if es_cliente_vip == "si":
    descuento = 20
    print("Descuento VIP: 20%")
elif cantidad >= 10:
    descuento = 15
    print("Descuento por cantidad: 15%")
elif cantidad >= 5:
    descuento = 10
    print("Descuento por cantidad: 10%")

# Calcular monto del descuento
monto_descuento = subtotal * (descuento / 100)
total = subtotal - monto_descuento

# Mostrar resumen
print("\n--- RESUMEN DE COMPRA ---")
print(f"Subtotal: Q{subtotal:.2f}")
print(f"Descuento ({descuento}%): -Q{monto_descuento:.2f}")
print(f"Total a pagar: Q{total:.2f}")