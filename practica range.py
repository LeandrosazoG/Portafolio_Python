

n= int(input("cuantos nombres desea ingresar"))


lista_nombres = []

for i in range(n):
    nombre = input(f"ingresa Los nombres #{i+1} : ")
    lista_nombres.append(nombre)


##buscar el nombre mas largo
nombre_mas_largo = max(lista_nombres, key=len)

print("Nombres ingresados",lista_nombres)
print("el nombre mas largo es ", nombre_mas_largo)













