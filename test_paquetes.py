import unittest
from main import GestionEnvios

class TestGestionEnvios(unittest.TestCase):
    def setUp(self):
        self.gestion = GestionEnvios()
    
    def test_agregar_paquete_valido(self):
        paquete = self.gestion.agregar_paquete(10, 5, 5, 2)
        self.assertEqual(len(self.gestion.paquetes), 1)
        self.assertEqual(str(paquete), "Paquete - Dimensiones: 10x5x5 cm, Peso: 2 kg")
    
    def test_agregar_paquete_invalido(self):
        with self.assertRaises(ValueError):
            self.gestion.agregar_paquete(0, 5, 5, 2)
    
    def test_mostrar_paquetes_vacio(self):
        self.assertEqual(self.gestion.mostrar_paquetes(), [])
    
    def test_mostrar_paquetes_con_datos(self):
        self.gestion.agregar_paquete(10, 5, 5, 2)
        self.assertEqual(self.gestion.mostrar_paquetes(), ["Paquete - Dimensiones: 10x5x5 cm, Peso: 2 kg"])

if __name__ == "__main__":
    unittest.main()
