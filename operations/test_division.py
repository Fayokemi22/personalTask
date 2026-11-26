from unittest import TestCase
from operations.division import divide

class Test(TestCase):

    def test_divide(self):
        a = 6
        b = 2
        result = divide(a, b)
        self.assertEqual(result, 3)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(6, 0)