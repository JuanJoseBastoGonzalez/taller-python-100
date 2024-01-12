def numero_intermedio():
    n1, n2, n3, media, menor, mayor = 0, 0, 0, 0, 0, 0
    print("INGRESE NÚMERO 01: ")
    n1 = int(input())
    print("INGRESE NÚMERO 02: ")
    n2 = int(input())
    print("INGRESE NÚMERO 03: ")
    n3 = int(input())
    if n1 > n2:
        mayor = n1
        menor = n2
    else:
        mayor = n2
        menor = n1

    if n3 > mayor:
        media = mayor
    elif n3 < menor:
        media = menor
    else:
        media = n3
    print("EL NÚMERO MEDIO ES:", media)
numero_intermedio()
