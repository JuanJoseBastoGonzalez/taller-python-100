def calcular_costo():
    horas = int(input("Ingrese las horas: "))
    minutos = int(input("Ingrese los minutos: "))
    segundos = int(input("Ingrese los segundos: "))
    tiempo_total_segundos = horas * 3600 + minutos * 60 + segundos
    tarifa_por_segundo = 0.25
    costo = tiempo_total_segundos * tarifa_por_segundo
    print("El costo total es: $", costo)
calcular_costo()
