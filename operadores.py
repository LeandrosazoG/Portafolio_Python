# # and: ambas condiciones deben ser True
# edad = 25
# tiene_licencia = True

# if edad >= 18 and tiene_licencia:
#     print("Puedes conducir")
# else:
#     print("No puedes conducir")




# # or: basta con que una condición sea True
# dia = "sábado"

# if dia == "sábado" or dia == "domingo":
#     print("Es fin de semana")
# else:
#     print("Es día de semana")





# # not: invierte el valor lógico
# es_mayor = True

# if not es_mayor:
#     print("Es menor de edad")
# else:
#     print("Es mayor de edad")




# ##operador not 


# bloqueado = input("¿Estás bloqueado? (sí/no): ").lower()

# if not bloqueado == "sí":
#     print("Puedes acceder al sistema")
# else:
#     print("Acceso denegado")




def acceso_vip():
    while True:
        try:
              edad = int(input("¿Cuál es tu edad?: "))
        except ValueError:
              print("debes ingresar numeros entero sin desimales")
              continue
         
        while True:
              bloqueado = input("¿Estás bloqueado? (sí/no): ").lower()
              if bloqueado in ["si","no"]:
                   break
              print("solo responde con si o con no")

        while True:
             invitado = input("¿Tienes invitación? (sí/no): ").lower()
             if invitado in ["si","no"]:
                break
             print("solo responde con si o con no ")

        while True:
              pase_especial = input("¿Tienes pase especial? (sí/no): ").lower()
              if pase_especial in ["si","no"]:
                 break
              print("solo responde con si o con un no ")


        if edad > 18 and bloqueado !="si" and (invitado =="si" or pase_especial =="si"):
            print("✅ Acceso concedido a la sala VIP")
            break
        else:
            print(" Acceso denegado")
            while True:
                intentar = input("quieres intentar nuevamente (si/no)").lower()
                if intentar in ["si", "no"]:
                    break
                print("solo responde 'si' o 'no")
            if intentar == "no":
                 print("adios")
                 break

         
  
   

acceso_vip()





