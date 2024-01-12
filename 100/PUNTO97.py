import random

def obtener_color_descuento():
    color = 0
    desct = 0
    compra = 0
    print("VALOR DE LA COMPRA: S/.")
    compra = float(input(""))
    print("Pulse una tecla...")
    tecla = input("")
    color = random.randint(1, 5)
    print("DESCUENTO:")
    if color == 1:
        print("COLOR: BLANCO")
        desct = 1
    elif color == 2:
        print("COLOR: VERDE")
        desct = 0.5
    elif color == 3:
        print("COLOR: NEGRO")
        desct = 0.4
    elif color == 4:
        print("COLOR: CELESTE")
        desct = 0.05
    elif color == 5:
        print("COLOR: ROJO")
        importe_descuento = compra * desct
    pago_final = compra - importe_descuento
    print(f"DESCUENTO: S/.{desct}")
    print(f"IMPORTE DESCUENTO: S/.{importe_descuento}")
    print(f"PAGO FINAL: S/.{pago_final}")
obtener_color_descuento()
