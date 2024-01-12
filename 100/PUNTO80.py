def calcular_bonificacion():
    venta = 0.0
    print("CALCULAR BONIFICACIÓN")
    print("INGRESE TOTAL DE VENTA S/.:")
    venta = float(input())
    print("\nBONIFICACIÓN:")
    if venta > 2000:
        print("BONIFICACIÓN 19%: S/.", (venta * 0.19))
    else:
        print("BONIFICACIÓN 50%: S/.", (venta * 0.50))
calcular_bonificacion()
