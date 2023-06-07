import unittest

class Calculadora:
    def somar(self, a, b):
        return a + b
    
    def subtrair(self, a, b):
        return a - b
    
    def multiplicar(self, a, b):
        return a * b
    
    def dividir(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Não é possível dividir por zero!")
        return a / b

class TestCalculadora(unittest.TestCase):
    def test_somar(self):
        c = Calculadora()
        self.assertEqual(c.somar(2, 3), 5)
        self.assertEqual(c.somar(-1, 5), 4)
        self.assertEqual(c.somar(0, 0), 0)
        
    def test_subtrair(self):
        c = Calculadora()
        self.assertEqual(c.subtrair(2, 3), -1)
        self.assertEqual(c.subtrair(-1, 5), -6)
        self.assertEqual(c.subtrair(0, 0), 0)
        
    def test_multiplicar(self):
        c = Calculadora()
        self.assertEqual(c.multiplicar(2, 3), 6)
        self.assertEqual(c.multiplicar(-1, 5), -5)
        self.assertEqual(c.multiplicar(0, 0), 0)
    
    def test_dividir(self):
        c = Calculadora()
        self.assertEqual(c.dividir(6, 3), 2)
        self.assertEqual(c.dividir(-10, 2), -5)
        self.assertRaises(ZeroDivisionError, c.dividir, 5, 0)
