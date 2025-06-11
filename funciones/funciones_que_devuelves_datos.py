def sumar(a,b):
    return a+b

resultado = sumar(3,5)
print(resultado)



##utilizacion real 

def aplicar_descuento(precio,descuento):
    return precio - (precio*descuento/100)








print(aplicar_descuento(1000,10))
aplicar_descuento(500,20)



def nombre(nombre):
    return nombre.capitalize()










def es_mayor_edad(nombre,edad):
    if edad >= 18:
        return f"{nombre} Eres mayor de edad, tu edad es {edad}"
    else:
        return f"{nombre} Eres menor de edad, tu edad es {edad}"

# Ahora sí, esto imprimirá solo el mensaje correcto
print(es_mayor_edad("juan",20))
print(es_mayor_edad("pedro",15))

