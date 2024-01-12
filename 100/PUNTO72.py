def login():
    usuario_correcto = "ADMIN"
    clave_correcta = 123456
    usuario = input("INGRESE USUARIO: ")
    clave = int(input("INGRESE CONTRASEÑA: "))
    if usuario == usuario_correcto and clave == clave_correcta:
        print("ACCESO PERMITIDO")
    else:
        print("ACCESO DENEGADO")
login()
