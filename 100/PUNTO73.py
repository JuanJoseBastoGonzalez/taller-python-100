def calcular_costo_llamada():
    duracion_llamada = 0
    costo_llamada = 0.0
    print("CANTIDAD DE MINUTOS:")
    duracion_llamada = int(input())
    if duracion_llamada <= 5:
        costo_llamada = duracion_llamada * 0.9
    else:
        costo_llamada = (5 * 0.9) + ((duracion_llamada - 5) * 0.5)
    print("EL COSTO ES:", costo_llamada)
calcular_costo_llamada()
