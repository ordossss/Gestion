###HERENCIA SIMPLE###################
class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad

    def hablar(self):
        return "Habalandodoooo"
    

class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad ,trabajo,salario):
        super().__init__(nombre,edad,nacionalidad )
        self.trabajo=trabajo
        self.salario=salario

luis=Empleado("Luis",20,"Veneco","Pre",1000)
print(luis.nombre)

###############HERENCIA MULTIPLE##################
class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad

    def hablar(self):
        return "Habalandodoooo"
    
class Artista:
    def __init__(self,habilidad):
        self.habilidad=habilidad

    def mostar_habilidad(self):
        return(f"mi hablidad es {self.habilidad}")


class EmpleadoArtista(Persona,Artista):
    def __init__(self,nombre,edad,nacionalidad,habilidad ,salario,empresa):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self,habilidad )
        self.empresa=empresa
        self.salario=salario

    def presentarse(self):
        return(f"{super().mostar_habilidad()} ")


luis=EmpleadoArtista("Luis",20,"Veneco","cantar",1000,"KNTEV")
print(luis.presentarse())