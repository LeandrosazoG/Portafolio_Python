
## Ejemplo 1: Recorrer una lista
frutas = ["manzanas", "banana","pera"]

for fruta in frutas :
    print(fruta)




## Ejemplo 2: Usar range() 
##ange(5) genera los números del 0 al 4 (¡no incluye el 5!).

for i in range(5):
    print(i)


##Ejemplo 3: range(inicio, fin, paso)
#inicio: 1

# fin: 10 (no se incluye)

# paso: 2 (de dos en dos)

for i in range(1,20,2):
    print(i)


##Ejemplo 4: Recorrer una cadena

nombre ="Leandro"

for letra in nombre :
    print(letra)


## Ejemplo práctico: Sumar todos los números del 1 al 10

suma = 0 

for numero in range (1,11):
    suma +=numero
print("suma es :",suma)



##break: interrumpe el bucle


for i in range(10):
    if i == 5:
        break
    print(i)




    