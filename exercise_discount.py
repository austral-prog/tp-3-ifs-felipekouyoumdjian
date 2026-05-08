def discount():
    precio = float(input())
    cantidad = int(input())
    subtotal = precio * cantidad

    if cantidad >= 10:
        descuento = 20 
    elif 5 <= cantidad <= 9:
        descuento = 10
    elif cantidad < 5:
        descuento = 0
    monto = subtotal * descuento / 100
    total = subtotal - monto

    print(f"Subtotal: {subtotal}")
    print(f"Descuento aplicado: {descuento}%")
    print(f"Monto de descuento: {monto}")
    print(f"Total final: {total}")

