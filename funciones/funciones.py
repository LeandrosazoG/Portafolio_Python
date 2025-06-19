# def saludar ():
#     print("hola mundo")


# saludar()



# def larry_descuento(precio,porcentaje):
#     descuento = precio*(porcentaje/100)
#     precio_final = precio-descuento
#     return precio_final

# total = larry_descuento(1000,0.15)

# print(f"el total a pagar es ${total :.2f}")



# def saludar(nombre):
#     return f"hola mundo,{nombre}"


# print(saludar("leandro"))



# def sumar(num1,num2):
#     resultado = num1+num2
#     return resultado


# sumar(1,2)
# print(sumar(1,2))



# def numero_mayor(num1,num2):
#     if num1 > num2:
#         return f"numero {num1} es mayor que numero{num2}"
#     elif num2 > num1:
#         return f"numero : {num2} es mayor que numero:{num1}"
#     else:
#         return "ambos numeros son iguales"


# print(numero_mayor(4,4))





def numero_mayor(num1,num2,num3):
    if num1 > num2  and num1 > num3:
        return f"el {num1} es mayor"
    elif num2 > num1  and num2 > num3:
        return f"el {num2}es mayor" 
    elif num3> num1  and num3 > num2:
        return f"el {num3} es mayor" 
    else:
        return f" los tres numeros son iguales"



print(numero_mayor(6, 8, 9))   # → El 9 es el mayor
print(numero_mayor(10, 5, 3))  # → El 10 es el mayor
print(numero_mayor(7, 7, 7)) 

