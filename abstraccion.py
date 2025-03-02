# # ################ decoradores, property , abstraccion ##################
# class Persona:
#     def __init__(self,nombre,edad):
#         self.__nombre=nombre
#         self.__edad=edad
    
#     @property #####sirve para el getter
#     def nombre(self):
#         return self.__nombre
    
#     @nombre.setter#####setter
#     def nombre(self,nombre_nuevo):
#         self.__nombre=nombre_nuevo

#     @nombre.deleter
#     def nombre(self):
#         del self.__nombre
        
      
# luis=Persona("Luis",21)
# nombre= luis.nombre ### no es necesario () ya que se usa property
# print(nombre)

# luis.nombre="Juan"### no es necesario () ya que se usa un decorador de setter
# nombre=luis.nombre
# print(nombre)

# del luis.nombre
################## ABSTRACCION #################METODOS ESPECIALES #############
from abc import ABC, abstractmethod

class Personas(ABC):
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractmethod
    def trabajar(self):
        pass

    def presentarse(self):
        print(f'Mi nombre es {self.nombre} y tengo {self.edad}')

class Estudiante(Personas):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def trabajar(self):
       print(f'YO HAGO {self.actividad}') 

    # def __str__(self):
    #     return 'ESTUDIANTEEEEEEEEE'
    
    def __repr__(self):
        return f'Estudiante("{self.nombre}", {self.edad}, "{self.sexo}", "{self.actividad}")'  

# Crear objeto
luis = Estudiante("LUIS", 21, "M", "NA")
# luis.trabajar()
# luis.presentarse()

# repre = repr(luis)
print(luis)
# Usar repr y eval
# repre = repr(luis)
# resultado = eval(repre)

# print(resultado.nombre)  # Debe imprimir "LUIS"

