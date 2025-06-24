import random as r

while True:
    print("bienvenido al juego de adivina el numero")

    numero_aletatorio = r.randint(1,100)
    intentos = 0

    while True:
        try:
            adivina = int(input("ingresa Numero al azar del 1 a 100 :  "))
            intentos+=1

            if adivina < 1 or adivina > 100:
                print("⚠️ El número debe estar entre 1 y 100.")
                continue

            if adivina == numero_aletatorio:
                print(f"🎉 ¡Correcto! Adivinaste el número en {intentos} intentos.")
                break
            elif adivina < numero_aletatorio:
                print("🔼 Pista: El número es mayor.")
            else:
                print("🔽 Pista: El número es menor.")
        except ValueError:
            print("ingresa solo numeros entero")

    repetir = input("¿INTENTAR OTRA VEZ?(S/N)").lower()
    if repetir !="s":
        print("Gracias por jugar mi juego  ")
        break
    
###  radom.randit te da un numero alateoro 

# ###import random: Importa la librería random que contiene las funciones para generar números aleatorios.
# random.randint(1, 100): Esta función genera un número entero aleatorio entre 1 y 100. Los argumentos 1 y 100 especifican el rango de números posibles.
# numero_aleatorio = ...: El número aleatorio generado se guarda en la variable numero_aleatorio.
# print(...): Imprime el valor de la variable, mostrando el número aleatorio generado.