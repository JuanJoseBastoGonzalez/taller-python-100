def cambiar_costo_seguro():
    print("TIPOS DE SEGURO:")
    print("1. X")
    print("2. Y")
    print("3. Z")
    print("OPCIÓN:")
    seguro = int(input())
    print("COSTO MENSUAL:")
    if seguro == 1:
        print("Pago mensual $5")
    elif seguro == 2:
        print("Pago mensual $30")
    elif seguro == 3:
        print("Pago mensual $15")
    else:
        print("Error en el tipo de seguro")
cambiar_costo_seguro()
