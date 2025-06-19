


def mostrar_usuario():
    for i,(id,nombre,tareas) in enumerate(usuarios):
        print(f"{i}.{nombre} (ID:{id}) - Tareas : {tareas}")



def agregar_tarea(indice_usuario,nueva_tarea):
    usuarios[indice_usuario[2]].append(nueva_tarea)


def eliminar_tarea(indice_usuario,tarea_a_eliminar):
    if tarea_a_eliminar in usuarios[indice_usuario][2]:
        usuarios[indice_usuario][2].remove(tarea_a_eliminar)
    else:
        print("tarea no encontrada")


def eliminar_nombre(indice_usuario,nombre_eliminar):
    if usuarios[indice_usuario][1] == nombre_eliminar:
        usuarios.pop(indice_usuario)
        print(f"Usuario '{nombre_eliminar}' eliminado.")
    else:
        print("Nombre no coincide. Usuario no eliminado.")


usuarios =[ (1,"Leandro",["instalar proyector"]),
           (2,"camila",["revisar sistema","enviar Infotme"]),
]




eliminar_tarea(0,"instalar proyector")

print(usuarios)