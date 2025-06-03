from menu_animal import mostrar_menu
from objeto_perro import Animal

mi_perro = Animal("Perro","BLACKY", "rojo", "doberman", 60, 50)
mi_gato =  Animal("Gato","Coco","negro","gato callejero",60,70)


def elegir_animal():
     while True:
         print("¿con que animal quiere interactuar?")
         print("\n 1 Perro")
         print("\n 2 Gato")
         eleccion = input("Elige una opcion(1 o 2, 3 para salir) : ")
         if eleccion == "1":
             return mi_perro
         elif eleccion == "2":
             return mi_gato
         elif eleccion == "3":
             print("saliste con exito del programa de animales🐾")
             return None
         else :
             print("opcion no valida.intenta denuevo.")

 
mascota = elegir_animal()
if mascota is None :
    print("Programa Finalizado")
    exit() 

acciones = {
    "1": mascota.atributos,
    "2": mascota.tiene_hambre,
    "3": mascota.comer,
    "4": mascota.cansado,
    "5": mascota.jugar,
    "6": mascota.dormir
}

while True:
    print(mostrar_menu())
    opcion = input("Selecciona una opción: ")
    if opcion == "0":
        print("¡Adiós! 🐾")
        break
    elif opcion in acciones:
        acciones[opcion]()
    else:
        print("Opción no válida. Intenta de nuevo.")
