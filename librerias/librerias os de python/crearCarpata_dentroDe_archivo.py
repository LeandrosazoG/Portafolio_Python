import os


#Nombre de la carpeta a crear
carpeta_destino ="librerias os de python" 


#Nombre del archivo
nombre_archivo = "archivo.txt"


##Contenido que queremos escribir en el archivo

contenido= "Este es el contenido del archivo."


##ruta de la carpeta de destino
ruta_archivo = os.path.join(os.getcwd(), carpeta_destino, nombre_archivo)



##crea y escribe en el archivo
with open(ruta_archivo,"w") as archivo:
    archivo.write(contenido)

print(f"Archivo '{nombre_archivo}' creado en: {ruta_archivo}")