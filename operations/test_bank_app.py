from unittest import TestCase
from operations import bank_app
from operations.bank_app import deposit, withdraw


class Test(TestCase):
    def setUp(self):
        bank_app.balance = 1000

    def test_deposit(self):
        self.assertEqual(2000, deposit(1000), globals())

    def test_withdraw(self):
        self.assertEqual(700, withdraw(300, "1234"), globals())

    def test_withdraw_wrong_pin(self):
        self.assertEqual("Wrong PIN", withdraw(300, "0000"), globals())

    def test_withdraw_insufficient_funds(self):
        self.assertEqual("Insufficient funds", withdraw(2000, "1234"), globals())