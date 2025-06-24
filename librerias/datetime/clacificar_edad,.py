
from datetime import datetime




while True:
    nombre =input("ingresa tu nombre :  ")
    fecha_nacimiento = input("ingrese su año de nacimiento (dd/mm/aaaa) : ")
    fecha_nacimiento= datetime.strptime(fecha_nacimiento, "%d/%m/%Y")

    hoy = datetime.now()
    edad = hoy.year -fecha_nacimiento.year

    if (hoy.month, hoy.day) == (fecha_nacimiento.month, fecha_nacimiento.day):
        print("🎉 ¡Hoy es tu cumpleaños, felicidades! 🎂")

    if (hoy.month,hoy.day) < (fecha_nacimiento.month,fecha_nacimiento.day ):
        edad-1
    

    if edad < 18 :
        print(f" estas en la adolecencia {nombre} y tu edad es {edad} ")
    elif edad >= 18 and edad <= 65:
       print(f"eres un adulto {nombre} y tu edad es {edad}")
    else:
         print(f"perteneces a la tercera edad {nombre} y tu edad es {edad}")
    
    repetir = input("¿INTENTAR OTRA VEZ?(S/N)").lower()
    if repetir !="s":
        print("Gracias por su preferencia ")
        break



##datetime.strptime() = función que interpreta (parsea) un string como fecha.
#hoy.year      # → el año actual (por ejemplo: 2025)
#hoy.month     # → el mes actual (por ejemplo: 5 para mayo)
#hoy.day       # → el día actual (por ejemplo: 28)
