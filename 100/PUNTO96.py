def calcular_costo_tecleado():
    print("Cantidad a comprar: ")
    cantidad = int(input())
    costo = 0
    print("Costo por teclado:")
    if cantidad in [1, 2, 3]:
        costo = 15
    elif cantidad in [4, 5, 6, 7, 8]:
        costo = 11
    else:
        costo = 10
    total_pagar = costo * cantidad

    print(f"Costo por teclado: S/.{costo}")
    print(f"Total a Pagar: S/.{total_pagar}")
calcular_costo_tecleado()
