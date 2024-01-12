def calcular_descuento():
    monto = 0.0
    descuento = 0.0
    print("MONTO DE COMPRA S/.")
    monto = float(input())
    if monto >= 350:
        descuento = monto * 0.35
        print("DESCUENTO ES DE 35%: S/.", descuento)
    else:
        descuento = monto * 0.10
        print("DESCUENTO ES DE 10%: S/.", descuento)
    monto_a_pagar = monto - descuento
    print("MONTO A PAGAR S/.:", monto_a_pagar)
calcular_descuento()
