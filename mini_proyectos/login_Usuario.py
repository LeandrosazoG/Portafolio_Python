######Login de usuario



nombre_usuario = "admin"
contrasena_usuario = "1234" 


intentos = 0
max_intentos = 3



while True:
    ### Solicitar al usuario que ingrese su nombre de usuario y contraseña
    nombre_usuario_ingresado = input("Ingrese su nombre de usuario: ")
    contrasena_ingresada= input("Ingrese su contraseña: ")
    ### Verificar si el nombre de usuario y la contraseña son correctos
    if nombre_usuario_ingresado == nombre_usuario and contrasena_ingresada == contrasena_usuario:
        print("¡Bienvenido al sistema!")
        break
    elif nombre_usuario_ingresado != nombre_usuario and contrasena_ingresada != contrasena_usuario:
        print("Nombre de usuario y contraseña incorrecta   Inténtalo de nuevo.")
        intentos += 1
    elif nombre_usuario_ingresado != nombre_usuario:
        print("Nombre de usuario incorrecto. Inténtalo de nuevo.")
        intentos += 1
        
    ### Verificar si se ha alcanzado el número máximo de intentos
    if intentos >= max_intentos:
        print(f"Demasiados intentos fallidos {max_intentos}. El programa se cerrará.")
        break


