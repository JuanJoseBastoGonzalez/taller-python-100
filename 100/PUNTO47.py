def calcular_dias_transcurridos():
    fecha_actual = int(input("Ingrese el día actual: "))
    factor_mes = int(input("Ingrese el factor del mes: "))
    dias_transcurridos = (factor_mes - 1) * 30 + fecha_actual
    print("Los días transcurridos son:", dias_transcurridos)
calcular_dias_transcurridos()
