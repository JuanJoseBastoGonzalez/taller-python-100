def ordenar_numeros():
    n1 = 0
    n2 = 0
    print("INGRESE PRIMER NÚMERO: ")
    n1 = int(input())
    print("INGRESE SEGUNDO NÚMERO: ")
    n2 = int(input())
    print("\nNÚMEROS ORDENADOS DE MAYOR A MENOR:")
    if n1 > n2:
        print(n1)
        print(n2)
    else:
        print(n2)
        print(n1)
ordenar_numeros()
