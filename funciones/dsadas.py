from datetime import datetime


def calularEdad(anio_nacimiento):
    anio_actual = datetime.now().year
    return anio_actual - anio_nacimiento


def esMayorEdad(anio_nacimiento):
    edad = calularEdad(anio_nacimiento)
    if  edad < 18:
        return f"eres menor de edad, tu edad es de {edad}"
    elif 18 <= edad <= 35:
        return f"eres mayor de edad, tu edad es de {edad}"
    elif 36 <= edad < 65:
        return f"Eres un adulto mayor, tu edad es de {edad}"
    elif  edad >=65:
        return f"eres de edad la tercera edad , tu edad es de {edad}"




print(esMayorEdad(2006)) 