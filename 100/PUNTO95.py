def nivel_academico():
    print("Ingrese Nota 1: ")
    N1 = float(input())
    print("Ingrese Nota 2: ")
    N2 = float(input())
    print("Ingrese Nota 3: ")
    N3 = float(input())
    prom = round((N1 + N2 + N3) / 3)
    print("NIVEL:")
    if prom <= 6:
        print("MALO")
    elif prom <= 10:
        print("REGULAR")
    elif prom <= 15:
        print("BUENO")
    else:
        print("EXCELENTE")
nivel_academico()
