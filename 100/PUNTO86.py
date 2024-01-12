def obtener_dia_semana():
    print("INGRESE DÍA [1-7]:")
    dia = int(input())
    print("DÍA DE LA SEMANA:")
    if dia == 1:
        print("LUNES")
    elif dia == 2:
        print("MARTES")
    elif dia == 3:
        print("MIÉRCOLES")
    elif dia == 4:
        print("JUEVES")
    elif dia == 5:
        print("VIERNES")
    elif dia == 6:
        print("SÁBADO")
    elif dia == 7:
        print("DOMINGO")
    else:
        print("Día Inválido")
obtener_dia_semana()
