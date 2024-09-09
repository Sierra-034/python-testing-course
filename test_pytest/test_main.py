import pytest

def test_isolated():
    assert True == True, 'True is not True'

class TestExample:
    def test_suma_dos_numeros(self):
        assert 10 + 10 == 20, 'Suma incorrecta'

    def test_resta_dos_numeros(self):
        assert 10 - 10 == 0, 'Resta incorrecta'


class TestExample2:
    def test_multiplicacion_dos_numeros(self):
        assert 10 * 10 == 100, 'Multiplicacion incorrecta'
