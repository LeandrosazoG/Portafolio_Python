def sumar(a,b):
    return a+b

resultado = sumar(3,5)
print(resultado)



##utilizacion real 

def aplicar_descuento(precio,descuento):
    return precio - (precio*descuento/100)








print(aplicar_descuento(1000,10))
aplicar_descuento(500,20)









nombre_usuario = input("Ingresa tu nombre: ")
edad_usuario = int(input("Ingresa tu edad: "))


def formatear_nombre(nombre):
    return nombre.strip().capitalize()





def es_mayor_edad(nombre,edad):
    nombre_formateado = formatear_nombre(nombre)
    if edad >= 18:
        return f"{nombre_formateado} Eres mayor de edad, tu edad es {edad}"
    else:
        return f"{nombre_formateado} Eres menor de edad, tu edad es {edad}"

# Ahora sí, esto imprimirá solo el mensaje correcto
mensaje = es_mayor_edad(nombre_usuario,edad_usuario)
print(mensaje)

