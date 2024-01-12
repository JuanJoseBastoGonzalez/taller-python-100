def verificar_paridad():
    num = int(input("INGRESE UN NÚMERO: "))
    C = num // 2
    r = 2 * C
    re = num - r
    if re == 0:
        print("NÚMERO PAR")
    else:
        print("NÚMERO IMPAR")
verificar_paridad()
