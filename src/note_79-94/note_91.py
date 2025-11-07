class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary

    # Add the __repr__() method
    def __repr__(self):
        emp_str = f"Employee({self.name} , {self.salary})"
        return emp_str

emp1 = Employee("Amar Howard", 30000)
print(repr(emp1))
emp2 = Employee("Carolyn Ramirez", 35000)
print(repr(emp2))