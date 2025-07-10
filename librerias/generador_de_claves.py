import random
import string
import secrets

longitud = int(input("¿Cuantos caractertes debe tener la contraseña?"))


caracteres = string.ascii_letters + string.digits + string.punctuation
contraseña = ''.join(secrets.choice(caracteres) for _ in range(longitud))

print((f"contraseña segura es : {contraseña}"))



# string.ascii_letters → contiene todas las letras del alfabeto (mayúsculas y minúsculas):
# 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# string.digits → contiene todos los números del 0 al 9:
# '0123456789'

# string.punctuation → contiene los símbolos comunes de puntuación:
# '!"#$%&\'()*+,-./:;<=>?@[\\]^_{|}~'`




