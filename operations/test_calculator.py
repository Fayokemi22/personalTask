from unittest import TestCase
from operations.calculator import Calculator


class TestCalculator(TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        # a = 12
        # b = 4
        # result = self.calc.add(a, b)
        self.assertEqual(16,self.calc.add(12, 4))

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(6, 2), 4)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(6, 2), 12)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 2), 3)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError) as context:
            self.calc.divide(5, 0)
        self.assertEqual(str(context.exception), "cannot be divided by zero")

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_add_decimals(self):
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3)