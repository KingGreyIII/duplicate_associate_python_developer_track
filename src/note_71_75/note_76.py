class Employee:
    # Create __init__() method
    def __init__(self, name, salary, amount):
        # Create the name and salary attributes
        self.name = name
        self.salary = salary
        self.amount = salary +  amount

    def monthly_salary(self):
        print("Gray")
        return self.salary / 12



emp = Employee("Korel Rossi", 2000, 1400)
print(emp.name)
print(emp.monthly_salary())