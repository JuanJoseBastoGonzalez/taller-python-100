def calcular_area_triangulo():
    print("ÁREA DEL TRIÁNGULO")
    b = float(input("BASE: "))
    h = float(input("ALTURA: "))
    area = (b * h) / 2
    print("ÁREA:", area, "cm²")
def calcular_perimetro_triangulo_equilatero():
    print("\nPERÍMETRO DEL TRIÁNGULO EQUILÁTERO")
    L = float(input("LADO: "))
    perimetro = 3 * L
    print("PERÍMETRO:", perimetro, "cm")
calcular_area_triangulo()
calcular_perimetro_triangulo_equilatero()
