
def calcular_iva(monto):
    return monto * 0.19

def total_a_pagar(precio,descuento):
    precio_con_descuento = precio - descuento
    iva = calcular_iva(precio_con_descuento)
    total = precio_con_descuento + iva
    return total


##llamamos a la funcion 
resultado = total_a_pagar(10000,2000)
print(f"El total a pagar es : {resultado}")