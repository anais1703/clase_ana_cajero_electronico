from base_de_datos import usuarios
is_on = True
while is_on:
    print("Bienvenido al banco davivienda")
    numero_cuenta = input("Ingrese su tarjeta : ")
    if numero_cuenta in usuarios:
        print(f"Bienvenido {usuarios[numero_cuenta]['nombre']}")
        input_contraseña = input("Ingrese su contraseña: ") 
    else: 
        print("Numero de cuenta invalido por favor intente nuevamente")
    