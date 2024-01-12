def calcular_costo_llamada():
    print("CLAVES DE DESTINO:")
    print("[1] Estados Unidos - $0.13")
    print("[2] Canada - $0.11")
    print("[5] America del Sur - $0.52")
    print("[6] America Central - $0.99")
    print("[8] Mexico - $0.17")
    print("[9] Europa - $0.17")
    print("[10] Asia - $0.20")
    print("[15] Africa - $0.59")
    print("[20] Oceania - $0.28")
    print("INGRESE CLAVE DESTINO:")
    clave = int(input())
    print("DURACIÓN DE LA LLAMADA (minutos):")
    minutos = int(input())
    print("COSTO DE LA LLAMADA:")
    if clave == 1:
        print(f"COSTO: ${minutos * 0.13}")
    elif clave == 2:
        print(f"COSTO: ${minutos * 0.11}")
    elif clave == 5:
        print(f"COSTO: ${minutos * 0.52}")
    elif clave == 6:
        print(f"COSTO: ${minutos * 0.99}")
    elif clave == 8 or clave == 9:
        print(f"COSTO: ${minutos * 0.17}")
    elif clave == 10:
        print(f"COSTO: ${minutos * 0.20}")
    elif clave == 15:
        print(f"COSTO: ${minutos * 0.59}")
    elif clave == 20:
        print(f"COSTO: ${minutos * 0.28}")
    else:
        print("¡¡ Error en clave !!")
calcular_costo_llamada()
