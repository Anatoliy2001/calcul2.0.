import unittest
from calcul import Fraction, FractionCalculator

class TestFraction(unittest.TestCase):
    def setUp(self):
        # Создаем исходные дроби для тестов
        self.fraction1 = Fraction(1, 2)
        self.fraction2 = Fraction(3, 4)

    def test_to_decimal(self):
        # Проверяем правильность преобразования дроби в десятичное число
        self.assertEqual(self.fraction1.to_decimal(), 0.5)
        self.assertEqual(self.fraction2.to_decimal(), 0.75)

class TestFractionCalculator(unittest.TestCase):
    def setUp(self):
        # Создаем экземпляр FractionCalculator для тестов
        self.calculator = FractionCalculator(Fraction(1, 2), Fraction(3, 4))

    def test_add(self):
        # Проверяем правильность сложения дробей
        result = self.calculator.add()
        self.assertEqual(result.numerator, 10)
        self.assertEqual(result.denominator, 8)

    def test_subtract(self):
        # Проверяем правильность вычитания дробей
        result = self.calculator.subtract()
        self.assertEqual(result.numerator, -2)
        self.assertEqual(result.denominator, 8)

    def test_multiply(self):
        # Проверяем правильность умножения дробей
        result = self.calculator.multiply()
        self.assertEqual(result.numerator, 3)
        self.assertEqual(result.denominator, 8)

    def test_divide(self):
        # Проверяем правильность деления дробей
        result = self.calculator.divide()
        self.assertEqual(result.numerator, 4)
        self.assertEqual(result.denominator, 6)

if __name__ == '__main__':
    unittest.main()