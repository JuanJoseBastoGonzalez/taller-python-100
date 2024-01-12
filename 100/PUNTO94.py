def asignar_bono_sueldo():
    print("Sueldo Base S/.")
    sueldo = float(input())
    print("Categoría: 1.A - 2.B - 3.C - 4.D : ")
    categoria = int(input())
    bonificacion = 0
    if categoria == 1:
        bonificacion = sueldo * 0.1
    elif categoria == 2:
        bonificacion = sueldo * 0.2
    elif categoria == 3:
        bonificacion = sueldo * 0.3
    elif categoria == 4:
        bonificacion = sueldo * 0.5
    print(f"BONIFICACIÓN : S/.{bonificacion}")
    print(f"SUELDO TOTAL: S/.{sueldo + bonificacion}")
asignar_bono_sueldo()
