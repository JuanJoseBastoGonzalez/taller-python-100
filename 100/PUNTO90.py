def operacion_aritmetica():
    print("NÚMERO 1:")
    num1 = float(input())
    print("NÚMERO 2:")
    num2 = float(input())
    print("OPERADOR [+,-,x,/] (1.-Suma, 2.-Resta, 3.-Multiplicación, 4.-División):")
    operador = int(input())
    print("RESULTADO:")
    if operador == 1:
        print("SUMA:", (num1 + num2))
    elif operador == 2:
        print("RESTA:", (num1 - num2))
    elif operador == 3:
        print("MULTIPLICACIÓN:", (num1 * num2))
    elif operador == 4:
        if num2 != 0:
            print("DIVISIÓN:", (num1 / num2))
        else:
            print("No se puede dividir por cero")
    else:
        print("Operador incorrecto")
operacion_aritmetica()
