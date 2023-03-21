import unittest

class TestExample(unittest.TestCase):

    def test_suma_numeros(self):
        numero_1 = 10
        numero_2 = 20
        resultado = numero_1 + numero_2

        self.assertEqual(resultado, 30)

    def test_resta_numeros(self):
        numero_1 = 30
        numero_2 = 20
        resultado = numero_1 - numero_2

        self.assertEqual(resultado, 10)


if __name__ == '__main__':
     unittest.main()
        