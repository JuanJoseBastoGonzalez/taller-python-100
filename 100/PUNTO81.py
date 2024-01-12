
precio = float(input("Ingrese el precio: S/."))
cant = int(input("Ingrese la cantidad: "))
IGV = 0
monto = 0
monto = precio * cant
if monto > 100:
    IGV = monto * 0.18
print("\nCALCULAR IGV SEGÚN EL MONTO DE COMPRA")
print("Precio: S/.", precio)
print("Cantidad:", cant)
print("Monto:", monto)
print("IGV 18%:", IGV)
print("TOTAL A PAGAR: S/.", monto + IGV)