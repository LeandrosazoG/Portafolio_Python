class Animal:


    def __init__(self,tipo,nombre,color,raza,hambre,energia):
        self.tipo = tipo
        self.nombre = nombre
        self.color = color
        self.raza = raza 
        self.hambre = hambre
        self.energia =  energia



    def atributos(self):
        print("tipo",self.tipo)
        print("nombre",self.nombre)
        print("color",self.color)
        print("raza",self.raza)
        print("hambre",self.hambre)
        print("energia",self.energia)


    def tiene_hambre(self):
        if self.hambre <= 80:
            print(f"tu perro {self.nombre} tiene Mucha hambre hambre ")
        elif self.hambre == 50:
            print(f"tu perro {self.nombre} tiene algo de hambre ")
        else:
            print(f"tu perro {self.nombre} no tiene hambre")


    def comer(self):
        print(f"tu mascota {self.nombre} esta comiendo 🐶 ")
        self.energia += 30
        self.hambre -= 40 ## baja el hambre

        if self.energia > 100:
            self.energia = 100
            print(f"Energia actual : {self.energia}")
            print(f"Energia actual : {self.hambre}")

    def cansado(self):
        if self.energia <= 20 :
            print(f"Tu mascota {self.nombre}, esta cansado 😴")
        else:
            print(f"tu mascota {self.nombre}, no esta cansado y quieree jugar  🐶")



    def jugar(self):
            print(f"{self.nombre} esta jugando")
            self.energia -= 30
            self.hambre +=20
            if self.energia < 0:
                self.energia = 0
                if self.hambre > 100:
                    self.hambre = 100
                print(f"Energía actual: {self.energia}")
                print(f"Hambre actual: {self.hambre}")    



    def dormir(self):
        print(f"tu perro esta decansado 😴")
        self.energia +=100
        self.hambre +=20
        if self.hambre > 100:
           self.hambre = 100
           print(f"Energia actual: {self.energia}")
           print(f"Hambre actual: {self.hambre}")


class Gato(Animal):
    
    def __init__(self, tipo, nombre, color, raza, hambre, energia):
        super().__init__(tipo, nombre, color, raza, hambre, energia)




    def maullar(self):
        print(f"el gato {self.nombre} dice Miau ")
