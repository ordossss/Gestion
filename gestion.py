class Envio:
    contador = 0  # Variable de clase para IDs únicos

    def __init__(self, alto, ancho, profundidad, peso):
        Envio.contador += 1
        self.id = Envio.contador
        self.alto = alto
        self.ancho = ancho
        self.profundidad = profundidad
        self.peso = peso

    def mostrar_envio(self):
        print(f"📦 Envio ID: {self.id}")
        print(f"   Dimensiones: {self.alto} x {self.ancho} x {self.profundidad} cm")
        print(f"   Peso: {self.peso} kg")
        print("-" * 30)


def main():
    envios = []

    while True:
        try:
            print("\n📦 Ingrese las dimensiones del envío:")
            alto = float(input("   Alto (cm): "))
            ancho = float(input("   Ancho (cm): "))
            profundidad = float(input("   Profundidad (cm): "))
            peso = float(input("   Peso (kg): "))

            envio = Envio(alto, ancho, profundidad, peso)
            envios.append(envio)

            print("\n✅ Envío registrado correctamente.\n")
            print("📋 Lista de envíos registrados:")
            for e in envios:
                e.mostrar_envio()

            opcion = input("\n¿Desea agregar otro envío? (s/n): ").strip().lower()
            if opcion != 's':
                break
        except ValueError:
            print("⚠️ Error: Ingrese valores numéricos válidos.")

    print("\n🚀 Gracias por usar el sistema de envíos. ¡Hasta luego!")
    print("/ADIOS")


if __name__ == "__main__":
    main()
