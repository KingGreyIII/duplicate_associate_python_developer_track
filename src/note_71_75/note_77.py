class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        # Check if salary is positive
        if salary is True:
            self.salary = salary
        else:
            self.salary = 0
            print("Invalid salary!")

    def give_raise(self, amount):
        self.salary += amount

    def monthly_salary(self):
        return self.salary / 12


emp = Employee("Korel Rossi", -1000)
print(emp.name)
print(emp.salary)