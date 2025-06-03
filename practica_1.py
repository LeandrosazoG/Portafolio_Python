while True:
    n = int(input("¿Cuántas edades vas a ingresar? "))
    if n > 0:
        break
    else:
        print("Debes ingresar un número mayor a 0.")

suma = 0
edad_mayor = -1
edad_menor = 100

for i in range(n):
    while True:
        edad = int(input(f"Ingrese edad #{i+1}: "))
        if edad > 0:
            break
        else:
            print("Debes ingresar una edad mayor a 0.")

    suma += edad

    if edad > edad_mayor:
        edad_mayor = edad
    if edad < edad_menor:
        edad_menor = edad

promedio = round(suma / n, 2)

print(f"\nEl promedio de edad es: {promedio}")
print(f"La edad mayor es: {edad_mayor}")
print(f"La edad menor es: {edad_menor}")
