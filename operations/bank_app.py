balance = 1000
pin = "1234"


def deposit(amount):
    global balance
    balance = balance + amount
    return balance


def withdraw(amount, entered_pin):
    global balance
    if entered_pin != pin:
        return "Wrong PIN"
    if amount > balance:
        return "Insufficient funds"
    balance = balance - amount
    return balance