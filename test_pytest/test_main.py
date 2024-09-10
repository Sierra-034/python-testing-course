import pytest

def test_isolated():
    assert True == True, 'True is not True'

class TestExample:

    @classmethod
    def setup_class(cls):
        print('>>> setup_class executes once before all methods')

    @classmethod
    def teardown_class(cls):
        print('>>> teardownd_class executes once after all methods')
    
    def setup_method(self):
        self.numero_uno = 10
        self.numero_dos = 20

    def teardown_method(self):
        print('>>> teardown_method executing')
    
    def test_suma_dos_numeros(self):
        assert self.numero_uno + self.numero_dos == 30, 'Suma incorrecta'

    def test_resta_dos_numeros(self):
        assert self.numero_uno - self.numero_dos == -10, 'Resta incorrecta'


class TestExample2:
    def test_multiplicacion_dos_numeros(self):
        assert 10 * 10 == 100, 'Multiplicacion incorrecta'
