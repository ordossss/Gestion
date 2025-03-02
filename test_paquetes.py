import unittest
from paquetes import GestionEnvios

class TestGestionEnvios(unittest.TestCase):

    def setUp(self):
        self.gestion = GestionEnvios()

    def test_agregar_paquete(self):
        paquete = self.gestion.agregar_paquete(10, 5, 8, 2)
        self.assertEqual(len(self.gestion.paquetes), 1)
        self.assertEqual(str(paquete), "Paquete - Dimensiones: 10x5x8 cm, Peso: 2 kg")

    def test_agregar_paquete_invalido(self):
        with self.assertRaises(ValueError):
            self.gestion.agregar_paquete(-10, 5, 8, 2)

    def test_mostrar_paquetes(self):
        self.gestion.agregar_paquete(12, 6, 10, 3)
        paquetes = self.gestion.mostrar_paquetes()
        self.assertEqual(paquetes, ["Paquete - Dimensiones: 12x6x10 cm, Peso: 3 kg"])

if __name__ == '__main__':
    unittest.main()
