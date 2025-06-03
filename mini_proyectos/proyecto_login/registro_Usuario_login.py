
## Registro de usuario
usuarios = {} # clave = nombre de usuario, valor = contraseña

def registrar_usuario(usuarios,nombre,contrasena):
    if nombre in usuarios:
        return False # ya existe un usuario con ese nombre
    usuarios[nombre] = contrasena
    return True # usuario registrado exitosamente



nombre_usuario = input("Ingrese su nombre de usuario: ")
contrasena_usuario = input("Ingrese su contraseña: ")

if registrar_usuario(usuarios, nombre_usuario, contrasena_usuario): 
    print("Usuario registrado exitosamente.")
else:
    print("El nombre de usuario ya está en uso. Por favor, elija otro nombre.") 




print("\n === Iniciar sesión ===")
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    nombre_ingresado = input("usuario: ")
    contrasena_ingresada = input("contraseña: ")

    if nombre_ingresado in usuarios and usuarios[nombre_ingresado] == contrasena_ingresada:
        print(f"¡Inicio de sesión exitoso, Bienvenido ! {nombre_ingresado}!")
        break
    else :
        print("nombre de uisuario o contraseña incorrectos. Inténtalo de nuevo.")
    intentos += 1
    

if intentos == max_intentos:
    print(f"Demasiados intentos fallidos ({max_intentos}). El programa se cerrará.")