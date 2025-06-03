import os 

carpeta_vieja = "nueva_carpeta"
carpeta_nueva = "librerias os de python"


ruta_actual = os.getcwd()
ruta_vieja = os.path.join(ruta_actual, carpeta_vieja)
ruta_nueva = os.path.join(ruta_actual, carpeta_nueva)



## verificamos si la carpeta vieja existe
if os.path.exists(ruta_vieja):
    os.rename(ruta_vieja, ruta_nueva)
    print(f"Carpeta renombrada de '{carpeta_vieja}' a '{carpeta_nueva}'")
else:
    print(f"La carpeta '{carpeta_vieja}' no existe en: {ruta_actual}")
    print("No se pudo renombrar la carpeta.")