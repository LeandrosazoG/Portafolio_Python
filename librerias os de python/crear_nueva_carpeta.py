import os



# Usa os.getcwd() para saber dónde estás.

# Usa os.path.join() para armar la ruta de la nueva carpeta.

# Verifica si ya existe con os.path.exists().

# Si no existe, la crea con os.mkdir().






nueva_carpeta = "nueva_carpeta"

##obtenmos la ruta absoluta de la carpeta
ruta_actual = os.getcwd()
ruta_nueva_carpeta = os.path.join(ruta_actual, nueva_carpeta)


##verificamos si la carpeta ya existe
if not os.path.exists(ruta_nueva_carpeta):
    os.mkdir(ruta_nueva_carpeta)
    print(f"Carpeta '{nueva_carpeta}' creada en: {ruta_nueva_carpeta}")
else:
    print(f"La carpeta '{nueva_carpeta}' ya existe en: {ruta_nueva_carpeta}")


