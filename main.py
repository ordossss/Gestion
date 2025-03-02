class Paquete:
    def __init__(self, largo, ancho, alto, peso):
        self.largo = largo
        self.ancho = ancho
        self.alto = alto
        self.peso = peso

    def __str__(self):
        return f"Paquete - Dimensiones: {self.largo}x{self.ancho}x{self.alto} cm, Peso: {self.peso} kg"

class GestionEnvios:
    def __init__(self):
        self.paquetes = []

    def agregar_paquete(self, largo, ancho, alto, peso):
        if largo <= 0 or ancho <= 0 or alto <= 0 or peso <= 0:
            raise ValueError("Las dimensiones y el peso deben ser mayores que 0.")
        paquete = Paquete(largo, ancho, alto, peso)
        self.paquetes.append(paquete)
        return paquete  # Retornar el paquete facilita las pruebas

    def mostrar_paquetes(self):
        return [str(paquete) for paquete in self.paquetes]

# Función de menú separada para evitar problemas en los tests
def menu():
    gestion = GestionEnvios()
    while True:
        print("\n Gestión de Paquetes")
        print("1 Agregar paquete")
        print("2️ Mostrar paquetes")
        print("3️ Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                largo = float(input("Ingrese el largo (cm): "))
                ancho = float(input("Ingrese el ancho (cm): "))
                alto = float(input("Ingrese el alto (cm): "))
                peso = float(input("Ingrese el peso (kg): "))
                gestion.agregar_paquete(largo, ancho, alto, peso)
                print("✅ Paquete registrado con éxito.")
            except ValueError:
                print("❌ Error: Ingrese valores numéricos válidos.")
        elif opcion == "2":
            paquetes = gestion.mostrar_paquetes()
            if not paquetes:
                print("No hay paquetes registrados.")
            else:
                print("\nLista de paquetes registrados:")
                for idx, paquete in enumerate(paquetes, 1):
                    print(f"{idx}. {paquete}")
        elif opcion == "3":
            print("👋 Saliendo del programa...")
            break
        else:
            print("⚠️ Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
