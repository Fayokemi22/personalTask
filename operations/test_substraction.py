from unittest import TestCase
from operations.substraction import divide, substract, multiply


class Test(TestCase):
    def test_substraction(self):
        a = 9
        b = 3
        result = substract(a, b)
        self.assertEqual(result, 6)

    def test_divide(self):
        a = 9
        b = 3
        result = divide(a, b)
        self.assertEqual(result, 3)

    def test_multiply(self):
        a = 9
        b = 3
        result = multiply(a, b)
        self.assertEqual(result, 27)


