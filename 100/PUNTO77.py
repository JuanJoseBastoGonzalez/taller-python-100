def calcular_sueldo_final():
    nombre = ""
    sueldoB = 0.0
    boni = 0.0
    sueldoF = 0.0
    hijos = 0
    print("CALCULAR EL SUELDO FINAL")
    print("Ingrese Nombre: ")
    nombre = input()
    print("Sueldo Básico S/.:")
    sueldoB = float(input())
    print("Nro. de Hijos: ")
    hijos = int(input())
    if hijos > 0:
        boni = sueldoB * 0.07
        sueldoF = sueldoB + boni
    print("\nBONIFICACIÓN:", boni)
    print("SUELDO FINAL:", sueldoF)
calcular_sueldo_final()
