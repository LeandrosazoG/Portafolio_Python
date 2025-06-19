
def calcular_descuento(precio,porcentaje):
    return precio *(porcentaje/100)

def calcularIva(monto):
   return monto*0.19


def calcularTotal(precio,porcentaje):
    descuento = calcular_descuento(precio,porcentaje)
    precio_con_descuento = precio - descuento
    iva = calcularIva(precio_con_descuento)
    total = precio_con_descuento + iva
    
    print(f"precio original {precio}")
    print(f"Precio original: ${precio}")
    print(f"Descuento: ${descuento}")
    print(f"Precio con descuento: ${precio_con_descuento}")
    print(f"IVA: ${iva}")
    print(f"Total a pagar: ${total}")
    return total
    

calcularTotal(10000, 20)


