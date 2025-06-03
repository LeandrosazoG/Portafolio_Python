# import math 

# def pedir_entero():
#     while True:
#         try :
#             valor = int(input("ingresa un numero entero :"))
#             print("numero entero valido",valor)
#             return valor
#         except  ValueError:
#             print("Error : debes ingeresar un numero entero valido")
      


# def pedir_float():
#     while True:
#         try :
#             valor2 = float(input("ingresa un numero  decimal :"))
#             print("numero entero valido",valor2)
#             break
#         except  ValueError:
#             print("Error : debes ingeresar un numero entero valido")
      

# resultado = pedir_entero()
# print("resultado devuelto",resultado)


#### validar  un imput tenga solo letras
# isalpha() devuelve True solo si la cadena tiene solo letras (sin espacios ni números).

# ##.strip()
# Elimina los espacios al principio y al final del texto ingresado.

# Ejemplo: si el usuario escribe " Juan ", .strip() lo convierte en "Juan".

def pedir_nombre():
    while True:
        nombre=input("ingresa tu nombnre : ").strip()
        if nombre.isalpha():
            print("nombre valido :",nombre)
            return nombre
        else:
            print("error : el nombre debe contener solo letras intenta otra vez")

resultado = pedir_nombre()

print(resultado)