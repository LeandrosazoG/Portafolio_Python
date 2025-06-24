import os 

#mostrar el directorio actua
ruta_actual = os.getcwd()
print(f"El directorio actual es: {ruta_actual}")


#listar los archivos y carpetas en el directorio actual
contenido = os.listdir(ruta_actual)
print("Contenido del directorio actual:")
for elemento in contenido:
    print(elemento)



print("\n Archivos encontrados:")
for elemento in contenido:
    ruta_elemento = os.path.join(ruta_actual,elemento)
    if os.path.isfile(ruta_elemento):
        print(f"Archivo: {elemento}")


print("\n Carpetas encontradas:")
for elemento in contenido:
    ruta_elemento = os.path.join(ruta_actual,elemento)
    if os.path.isdir(ruta_elemento):
        print(f"Carpeta: {elemento}")
 


