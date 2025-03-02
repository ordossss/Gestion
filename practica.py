class Celular:
    #Constructor
    def __init__(self,marca,modelo,camara):
        self.marca=marca
        self.modelo=modelo
        self.camara=camara
    #metodos
    def llamar(self): #el self hace referencia al objeto 
       return(f'Esta llamando desde un {self.modelo}')
 
celular1=Celular("Samsung","S23","48")
print(celular1.modelo)
print(celular1.llamar())

class Estudiantes:
    def __init__(self,nombre,edad,grado):
        self.nombre=nombre
        self.edad=edad
        self.grado=grado

    def estudiar(self):
        return ("Estudiando")

    def __str__(self):#Esto se mostrara cuando se imprima el objeto
        return (f"Nombre: {self.nombre}\nEdad: {self.edad}")


nombre=input("Digite su nombre: ")
edad=input("Digite su edad: ")
grado=input("Grado: ")
estudiante1=Estudiantes(nombre,edad,grado)

print(f'Datos:\nNombre: {estudiante1.nombre}\nEdad: {estudiante1.edad}')

while True:
    estudiar=input("Digite:   ")
    if estudiar.lower()=="estudiar":
        print(estudiante1.estudiar())
        break
print("\n\n")
print(estudiante1)

############################CON PEP8 #########################################3
class Celular:
    """Clase que representa un celular."""

    def __init__(self, marca, modelo, camara):
        """Constructor de la clase Celular."""
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        """Método para realizar una llamada."""
        return f'Está llamando desde un {self.modelo}'


celular1 = Celular("Samsung", "S23", "48")
print(celular1.modelo)
print(celular1.llamar())


class Estudiante:
    """Clase que representa a un estudiante."""

    def __init__(self, nombre, edad, grado):
        """Constructor de la clase Estudiante."""
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        """Método que representa la acción de estudiar."""
        return "Estudiando"

    def __str__(self):
        """Representación en cadena del objeto."""
        return f"Nombre: {self.nombre}\nEdad: {self.edad}"


# Solicitar datos del usuario
nombre = input("Digite su nombre: ")
edad = input("Digite su edad: ")
grado = input("Grado: ")

# Crear instancia de la clase Estudiante
estudiante1 = Estudiante(nombre, edad, grado)

print(f'Datos:\nNombre: {estudiante1.nombre}\nEdad: {estudiante1.edad}')

# Bucle para verificar la acción "estudiar"
while True:
    estudiar = input("Digite: ").strip().lower()
    if estudiar == "estudiar":
        print(estudiante1.estudiar())
        break

print("\n\n")
print(estudiante1)