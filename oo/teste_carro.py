from unittest import TestCase
from oo.carro import Motor

class CarroTesteCase(TestCase):
    def teste_velocidade_inicial(self):
        motor=Motor()
        self.assertEqual(0, motor.velocidade)