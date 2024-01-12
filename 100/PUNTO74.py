def es_capicua():
    num = 0
    c1 = 0
    r1 = 0
    c2 = 0
    r2 = 0
    print("INGRESE NÚMERO DE 3 CIFRAS:")
    num = int(input())
    r1 = num % 100
    c1 = (r1 - (r1 % 10)) / 10
    r2 = r1 % 10
    c2 = (num - (r2 * 100 + c1 * 10)) / 10
    if num == ((r2 * 100) + (c2 * 10) + c1):
        print("NÚMERO CAPICÚA")
    else:
        print("NO ES CAPICÚA")
es_capicua()
