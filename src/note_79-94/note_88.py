#conditional statement commences
class BankAccount:
    # Modify to initialize a number attribute
    def __init__(self, number, balance=0):
        self.balance = balance
        self.number = number

    def withdraw(self, amount):
        self.balance -= amount

        # Define __eq__ that returns True if the number attributes are equal

    def __eq__(self, number):
        return self.number == number.number

    # Create accounts and compare them


acct1 = BankAccount(123, 1000)
acct2 = BankAccount(123, 1000)
acct3 = BankAccount(456, 1000)
print(acct1 == acct2)
print(acct1 == acct3)
