lista_notas = []

while True:
    print("\nMenú de opciones:"
          "\n1. Agregar notas"
          "\n2. Eliminar notas"
          "\n3. Salir")
    
    try:
        opcion = int(input("Ingrese la opción que desea: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    if opcion == 1:
        try:
            n = int(input("¿Cuántas notas desea ingresar?: "))
            for i in range(n):
                nota = int(input(f"Ingrese la nota {i + 1}: "))
                lista_notas.append(nota)
            print("Notas actuales:", lista_notas)
        except ValueError:
            print("Debe ingresar solo números.")
    
    elif opcion == 2:
        if not lista_notas:
            print("No hay notas para eliminar.")
            continue
        print("Notas actuales:", lista_notas)
        try:
            n = int(input("¿Cuántas notas desea eliminar?: "))
            for i in range(n):
                nota = int(input(f"Ingrese la nota a eliminar ({i + 1}): "))
                if nota in lista_notas:
                    lista_notas.remove(nota)
                else:
                    print(f"La nota {nota} no se encuentra en la lista.")
            print("Notas actuales:", lista_notas)
        except ValueError:
            print("Debe ingresar solo números.")
    
    elif opcion == 3:
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
  


