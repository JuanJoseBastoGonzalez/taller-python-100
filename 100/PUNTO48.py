def descomponer_numero():
    num = int(input("Ingrese un número de tres cifras: "))
    cen = (num - (num % 100)) / 100
    res = num % 100
    dec = (res - (res % 10)) / 10
    uni = res % 10
    print("CENTENA:", int(cen))
    print("DECENA:", int(dec))
    print("UNIDAD:", int(uni))
descomponer_numero()
