from unittest import TestCase
from operations.division import divide

class Test(TestCase):

    def test_divide(self):
        a = 6
        b = 2
        # result = divide(6, 2)
        self.assertEqual(3,divide(6, 2))

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(6, 0)