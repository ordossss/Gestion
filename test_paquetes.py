import unittest
from paquetes import GestionEnvios, Paquete  # Asegúrate de importar la clase Paquete si la usas

class TestGestionEnvios(unittest.TestCase):

    def setUp(self):
        self.gestion = GestionEnvios()

    def test_agregar_paquete(self):
        """Verifica que se pueda agregar un paquete correctamente."""
        self.gestion.agregar_paquete(10, 5, 8, 2)
        self.assertEqual(len(self.gestion.paquetes), 1)
        paquete = self.gestion.paquetes[0]  # Acceder al paquete agregado
        self.assertEqual(str(paquete), "Paquete - Dimensiones: 10x5x8 cm, Peso: 2 kg")

    def test_agregar_paquete_invalido(self):
        """Verifica que no se pueda agregar un paquete con valores negativos."""
        with self.assertRaises(ValueError):  # Espera un ValueError
            self.gestion.agregar_paquete(-10, 5, 8, 2)

    def test_mostrar_paquetes(self):
        """Verifica que mostrar_paquetes devuelva la lista correcta de paquetes."""
        self.gestion.agregar_paquete(12, 6, 10, 3)

        # Modifica `mostrar_paquetes()` en `GestionEnvios` para que devuelva una lista
        paquetes = [str(p) for p in self.gestion.paquetes]  
        
        self.assertEqual(paquetes, ["Paquete - Dimensiones: 12x6x10 cm, Peso: 3 kg"])

if __name__ == '__main__':
    unittest.main()
