# Define and initialize the Calculator class
class Calculator:
    def __init__(self, num_one, num_two):
        self.num_one = num_one
        self.num_two = num_two

    # Create the addition method
    def addition(self):
        return self.num_one + self.num_two

    # Create the subtraction method
    def subtraction(self):
        return self.num_one - self.num_two

    # Create the multiplication method
    def multiplication(self):
        return self.num_one * self.num_two

calc = Calculator(10, 5)

print(calc.addition())       # ➜ 15
print(calc.subtraction())    # ➜ 5
print(calc.multiplication()) # ➜ 50
