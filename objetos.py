class Personaje:
   
      #dos guiones bajos hace mi clase privada 

    #   get_...() → obtener el valor (getter)
    #   set_...() → modificar el valor (setter)


    
    def __init__(self,nombre,fuerza,inteligencia,defensa,vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida


    def atributos(self):
        print(self.nombre,":",sep="")
        print("Fuerza:",self.fuerza)
        print("inteligencia:",self.inteligencia)
        print("Defensa:",self.defensa)
        print("Vida:",self.vida)
    

    def subir_nivel(self,fuerza,inteligencia,defensa):
        self.fuerza = self.fuerza+fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa


    def esta_vivo(self):
        return self.vida > 0
    

    def morir(self):
        self.vida = 0
        print(self.nombre,"ha muerto")

    def daño(self,enemigo):
        return self.fuerza - enemigo.defensa
    

    def atacar(self,enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre,"ha realizado",daño,"puntos de daño a",enemigo.nombre)
        if enemigo.esta_vivo():
            print("la vida de",enemigo.nombre,"es",enemigo.vida)
        else:
            enemigo.morir()


    def get_fuerza(self):
        return  self.fuerza
    

    def set_fuerza(self,fuerza):
        if fuerza < 0 :
            print("error,has introducido un valor negativo")
        else:
            self.fuerza =  fuerza


##herencia
class Guerrero(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida,espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        opcion=int(input("Elige un arma :(1) Acero valyrio, daño 8. (2)MataDragones,daño 10 :"))
        if opcion == 1:
           self.espada = 8
        elif opcion == 2:
           self.espada = 10
        else:
           print("numero de arma incorrecto")

    def atributos(self):
        super().atributos()
        print("espada",self.espada)
       
    
    def daño(self,enemigo):
        return self.fuerza*self.espada - enemigo.defensa
    


class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida,libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print("libro",self.libro)


    def daño(self,enemigo):
        return self.inteligencia * self.libro - enemigo.defensa





Personaje_1 = Guerrero("Guts",20,10,4,100,4)
personaje_2 = Mago("darkleo",5,15,4,100,3)


def combate(jugador_1,jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print(" \nTurno",turno)
        print(">>>Accion de ",jugador_1.nombre, ":",sep="")
        jugador_1.atacar(jugador_2)
        print(">>>Accion de ",jugador_2.nombre, ":",sep="")
        jugador_2.atacar(jugador_1)
        turno = turno  + 1 
    
    if jugador_1.esta_vivo():
        print("\nHa GANADO",jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\Ha Ganado",jugador_2.nombre)


combate(Personaje_1, personaje_2)




# guts = Guerrero("guts",20,10,10,100,6)      
# goku= Personaje("leandro",10,1,3,100)
# leo =  Mago("darkleo",3,10,4,6,20)





# mi_enemigo = Personaje("enemy stando",8,5,3,5)





# mi_personaje.atacar(mi_enemigo)
# mi_enemigo.atributos()
# print(mi_personaje.daño(mi_enemigo))
# print(mi_personaje.esta_vivo())
# mi_personaje.atributos()
# mi_personaje.subir_nivel(1,2,0)
# mi_personaje.atributos()


# ##modificar 
# ##mi_personaje.nombre = "leandro"
# ##mi_personaje.fuerza = 10
# print("el nombre del juegador es : ",mi_personaje.nombre)
# print("La fuerza del juegador es : ",mi_personaje.fuerza)