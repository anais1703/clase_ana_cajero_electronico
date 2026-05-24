from base_de_datos import usuarios
is_on = True
while is_on:
    print("Bienvenido al banco davivienda")
    numero_cuenta = input("Ingrese su tarjeta : ")
    if numero_cuenta in usuarios:
        print(f"Bienvenido {usuarios[numero_cuenta]['nombre']}")
        input_contraseña = input("Ingrese su contraseña: ") 
        if input_contraseña == usuarios[numero_cuenta]["pin"]:
            sesion_abierta = True
            while sesion_abierta:
                print("Elija una opcion: ")
                print("1. Consulta de saldo")
                print("2. retiro")
                print("3. deposito")
                print("4. salir")
                opcion = int (input ("ingrese un numero del 1 al 4: "))
                
                if opcion == 1:
                    print(f"su saldo es: {usuarios[numero_cuenta]['saldo']}")

                elif opcion == 2: 
                    saldo = usuarios[numero_cuenta]['saldo']
                    monto_de_retiro = int(input("Ingrese el monto a retirar: "))
                    if monto_de_retiro > saldo:
                        print("saldo insuficiente")
                    else:

                        saldo = saldo - monto_de_retiro
                        usuarios[numero_cuenta]["saldo"] = saldo
                        print(f"su nuevo saldo es : {usuarios[numero_cuenta]['saldo']}")
                elif opcion == 3:
                    saldo = usuarios[numero_cuenta]['saldo']
                    monto_de_deposito = int(input("Ingrese el monto a depositar: "))
                    saldo = saldo + monto_de_deposito
                    usuarios[numero_cuenta]["saldo"] = saldo
                    print(f"su nuevo saldo es : {usuarios[numero_cuenta]['saldo']}")
                elif opcion == 4:
                    print("hasta luego")
                    sesion_abierta = False

        else: 
            print("Contraseña incorrecta por favor intente nuevamente")
    else: 
        print("Numero de cuenta invalido por favor intente nuevamente")
    