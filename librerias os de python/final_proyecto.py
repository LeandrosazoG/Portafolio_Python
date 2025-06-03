import os

 
print("\nmenu de opciones"
      "\n1. Mostrar el directorio actual"
      "\n2. Listar los archivos y carpetas en el directorio actual"
      "\n3. crear una carpeta nueva"
      "\n4. renombrar una carpeta existente"
      "\n5. crear un archivo de texto en la carpeta actual"
      "\n6. leer un archivo de texto en la carpeta actual"
      "\n7. eliminar un archivo de texto de la carpeta actual"
      "\n8. eliminar una carpeta existente"
      "\n9. Salir")




while True:
      print("\nmenu de opciones"
      "\n1. Mostrar el directorio actual"
      "\n2. Listar los archivos y carpetas en el directorio actual"
      "\n3. crear una carpeta nueva"
      "\n4. renombrar una carpeta existente"
      "\n5. crear un archivo de texto en la carpeta actual"
      "\n6. leer un archivo de texto en la carpeta actual"
      "\n7. eliminar un archivo de texto de la carpeta actual"
      "\n8. eliminar una carpeta existente"
      "\n9. Salir")

      opcion = int(input("Seleccione una opcion: "))
      if opcion == 1:
            ruta_actual = os.getcwd()
            print(f"El directorio actual es {ruta_actual}")
            
      elif opcion == 2:
            contenido = os.listdir(os.getcwd())
            for elemento in contenido:
                  print(f"estos elementos estan en el directorio actual: {elemento}")
            
      elif opcion == 3:
            nueva_carpeta = input("ingresa el nombre de la carpeta nueva:")
            ruta_actual= os.getcwd()
            ruta_nueva_carpeta = os.path.join(ruta_actual, nueva_carpeta)
            if not os.path.exists(ruta_nueva_carpeta):
                  os.mkdir(ruta_nueva_carpeta)
                  print(f"carpeta {nueva_carpeta} creada en {ruta_nueva_carpeta}")
            else:
                  print(f"La carpeta {nueva_carpeta} ya existe en {ruta_nueva_carpeta}")
            
      elif opcion == 4:
            carpeta_actual = input("ingresa el nombre de la carpeta a renombrar:")
            carpeta_renombrada= input("ingresa el nuevo nombre de la carpeta:")
            ruta_actual = os.getcwd()
            ruta_vieja = os.path.join(ruta_actual,carpeta_actual)
            ruta_nueva = os.path.join(ruta_actual, carpeta_renombrada)
            if os.path.exists(ruta_vieja):
                  os.rename(ruta_vieja, ruta_nueva)
                  print(f"carpeta renombrada de {carpeta_actual} a {carpeta_renombrada}")
            else:
                  print(f"La carpeta {carpeta_actual} no existe en {ruta_actual}")
                  print("No se pudo renombrar la carpeta.")
            
      elif opcion == 5:
            carpeta_destino = input("ingresa el nombre de la carpeta donde quieres crear el archivo:")
            nombre_archivo = input("ingresa el nombre del archivo a crear:")
            contenido = input("ingresa el contenido de tu archivo texto:")
            ruta_archivo = os.path.join(os.getcwd(), carpeta_destino, nombre_archivo)
            with open(ruta_archivo, "w") as archivo:
                  archivo.write(contenido)
            print(f"Archivo '{nombre_archivo}' creado en: {ruta_archivo}")
            
      if opcion == 6:
            carpeta = input("ingresa el nombre de la carpeta donde se encuentra el archivo:")
            nombre_archivo = input("ingresa el nombre del archivo a leer:")
            ruta = os.path.join(os.getcwd(),carpeta,nombre_archivo)
            with open(ruta, "r", encoding="utf-8") as file:
                  contenido = file.read()
                  print(f"Contenido del archivo '{nombre_archivo}':\n{contenido}")
            
      elif opcion == 7:
            carpeta = input("ingresa el nombre de la carpeta donde se encuenta el archivo:")
            nombre_archivo = input("ingresa el nombre del archivo a eliminar:")
            ruta = os.path.join(os.getcwd(), carpeta, nombre_archivo)
            if os.path.exists(ruta):
                  os.remove(ruta)
                  print(f"Archivo '{nombre_archivo}' eliminado de: {ruta}")
            else:
                  print(f"El archivo '{nombre_archivo}' no existe en: {ruta}")
            
      elif opcion == 8:
            carpeta = input("ingresa el nombre de la carpeta a eliminar:")
            ruta =os.path.join(os.getcwd(), carpeta)
            if os.path.exists(ruta):
                  os.rmdir(ruta)
                  print(f"Carpeta '{carpeta}' eliminada de: {ruta}")
            else:
                  print(f"La carpeta '{carpeta}' no existe en: {ruta}")
            
      repetir = input("¿Deseas realizar otra operación? (s/n): ").lower()
      if repetir !="s":
            print("Gracias por usar el programa. ¡Hasta luego!")
            break

