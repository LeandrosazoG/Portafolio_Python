while True:
    print("\nMenu calculadora Comun"
      "\n1 para sumar"
      "\n2 para restar"
      "\n3 para multiplicar"
      "\n4 para division")


    while True:
        try:
            opciones = int(input("ingresa la opcion que deseas : "))
            if opciones < 1 or opciones > 4:
                print("por favor, elige una opcion valida (1 a 4)")
                continue
            break
        except ValueError:
            print("ingresa un numero entero")

    numero1 = int(input("ingresa un numero :  "))
    numero2 = int(input("ingresa el numero : "))


    if opciones == 1:
        resultado = numero1+numero2
        print(f"el resultadod e la suma es :{resultado}")
    elif opciones == 2:
        resultado = numero1 - numero2
        print(f"el resultado de la resta es : {resultado}")
    elif opciones == 3 :
        resultado = numero1*numero2
        print(f"el resultado de tu multiplicacion es : {resultado}")
    elif opciones == 4:
        if numero2 == 0:
            print("numero no se puede dividir por 0.")
        else:
            resultado = numero1/numero2 
            print(f" el resultado de {numero1} / {numero2} = {resultado}")

    repetir = input("¿desea otra operacion?(s/n)").lower()
    if repetir !="s":
        print("Gracias por usar la calculadora")
        break
    