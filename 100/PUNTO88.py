def mostrar_estacion():
    print("NÚMERO [1-4]:")
    estacion = int(input())
    print("ESTACIÓN DEL AÑO:")
    if estacion == 1:
        print("Es Verano")
    elif estacion == 2:
        print("Es Otoño")
    elif estacion == 3:
        print("Es Invierno")
    elif estacion == 4:
        print("Es Primavera")
    else:
        print("Estación no válida")
mostrar_estacion()
