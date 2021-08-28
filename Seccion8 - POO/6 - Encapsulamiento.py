# No existe encapsulamiento como tal pero se puede simular uno

class encapsulamiento:
    __atributo_priv = "Atributo privado (no se le tiene acceso fuera de la clase)"

    def __privado_net(self):
        print("Soy un método que no vas a poder acceder desde afuera de la clase")

e = encapsulamiento()
#print(e.__atributo_priv_)
#print(e.__privado_net)

class encapsulamiento2:
    __atributo_priva = "Atributo privado (no se le tiene acceso fuera de la clase)"

    def __privado_met(self):
        print("Soy un método que no vas a poder acceder desde afuera de la clase")

    def atributo_pub(self):
        print(self.__atributo_priva)

    def public_met(self):
        return self.__privado_met()

e2 = encapsulamiento2()
e2.atributo_pub()
e2.public_met()