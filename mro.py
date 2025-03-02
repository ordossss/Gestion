#el MRO trata de una lista de clases que indica el orden en que Python busca atributos y métodos. 
#El MRO es fundamental en la herencia múltiple, ya que un mismo método puede estar presente en varias superclase
 #POLIMORFISMOOOOOOOOO
class Animal:
    def sonido(self):
        pass
class Gato(Animal):
    def sonido(self):
        return "Miua"
    
class Perro(Animal):
    def sonido(self):
        return "Guau"
    
def hacer_sonido(animal):
    print(animal.sonido())

gato=Gato()
perro=Perro()

print(gato.sonido())
hacer_sonido(perro)

#######################################
#Encapsulamiento 
class Clase:
    def __init__(self):
        self._priv="valor"  """" atributo privado"""
        self.__privado="valor privado" """" atributo muy muy privado"""

############### quede en getter y setters

         
