import os

## nombre del archivo a leer
carpeta="librerias os de python"
nombre_archivo = "archivo.txt"


##obtener la ruta del archivo
ruta = os.path.join(os.getcwd(), carpeta, nombre_archivo)


with open(ruta, "r", encoding="utf-8") as file:
    contenido = file.read() 
    print(f"Contenido del archivo '{nombre_archivo}':\n{contenido}")
    