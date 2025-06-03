


print("\nBienvenido A calculadora de IMC")

while True:
    try:
        peso = int(input("Ingresa tu peso kg: "))
        if peso <= 0 :
            print("ingrese un peso mayor a cero")
            continue
        break
    except ValueError:
        print("por favoer, ingresa solo numero enteros sin desimales")
    

while True:
    try:
        altura = float(input("Ingresa tu estatura mt: "))
        if altura <= 0 :
            print("ingrese una altura mayor a cero")
            continue
        break
    except ValueError:
        print("ingrese valores decimales por altura")

        
imc = peso / (altura ** 2)

if imc < 18.5 :
    print(f"tu imc esta en rango bajo con un imc de {imc}")
elif imc > 18.5 and imc <=24.9:
     print(f"tu imc se encuentra en rangos normales con un imc de {imc}")
elif imc > 25 and  imc  <=29.9:
    print(f"tu imc se encuentra en rango sobres peso con un imc de {imc}")
else:
    print(f"print tu imc se encuetra en rangos de obeso con un imc de {imc}")


# 



