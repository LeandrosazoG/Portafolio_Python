import os 

carpeta = "librerias os de python"
nombre_archivo = "archivo.txt"

##ruta del archivo a eliminar
ruta =os.path.join(os.getcwd(), carpeta, nombre_archivo)

##verificamos si el archivo existe
if os.path.exists(ruta):
    os.remove(ruta)
    print(f"Archivo '{nombre_archivo}' eliminado de: {ruta}")
else:
    print(f"El archivo '{nombre_archivo}' no existe en: {ruta}")
