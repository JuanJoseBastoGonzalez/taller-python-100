def calcular_costo_tecleado():
    cantidad = 0
    costo = 0.0
    print("INGRESE CANTIDAD A COMPRAR: ")
    cantidad = int(input())
    if cantidad in [1, 2, 3]:
        costo = 15
    elif cantidad in [4, 5, 6, 7, 8]:
        costo = 11
    else:
        costo = 10
    print(f"COSTO POR TECLADO: S/.{costo}")
    print(f"TOTAL A PAGAR: S/.{costo * cantidad}")
calcular_costo_tecleado()
