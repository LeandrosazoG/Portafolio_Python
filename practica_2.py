def acceso_vip():
    while True:
        try:
            edad = int(input("¿Cuál es tu edad?: "))
            if edad <= 0:
                print("⚠️ La edad debe ser mayor que cero.")
                continue
        except ValueError:
            print("❌ Debes ingresar solo números enteros sin decimales.\n")
            continue

        while True:
            bloqueado = input("¿Estás bloqueado? (sí/no): ").lower()
            if bloqueado in ["si", "no"]:
                break
            print("⚠️ Solo responde con 'si' o 'no'.")

        while True:
            invitado = input("¿Tienes invitación? (sí/no): ").lower()
            if invitado in ["si", "no"]:
                break
            print("⚠️ Solo responde con 'si' o 'no'.")

        while True:
            pase_especial = input("¿Tienes pase especial? (sí/no): ").lower()
            if pase_especial in ["si", "no"]:
                break
            print("⚠️ Solo responde con 'si' o 'no'.")

        if edad > 18 and bloqueado != "si" and (invitado == "si" or pase_especial == "si"):
            print("✅ Acceso concedido a la sala VIP")
            break
        else:
            print("❌ Acceso denegado.")
            while True:
                retry = input("¿Quieres intentar nuevamente? (sí/no): ").lower()
                if retry in ["si", "no"]:
                    break
                print("⚠️ Solo responde con 'si' o 'no'.")
            if retry == "no":
                print("Adiós!")
                break

acceso_vip()

