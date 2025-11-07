# class Employee:
#     def __init__(self, name, salary=30000):
#         self.name = name
#         self.salary = salary
#
#
# class Manager(Employee):
#     def __init__(self, name, salary=50000, project=None):
#         # Option 1: manual
#         # Employee.__init__(self, name, salary)
#
#         # Option 2: preferred
#         super().__init__(name, salary)
#         self.project = project
#
#
# m = Manager("Debbie", 70000, "AI Integration")
# print(m.name)       # Debbie
# print(m.salary)     # 70000
# print(m.project)    # AI Integration

# original code
class Employee:
    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount


class Manager(Employee):
    # Add a constructor
    def __init__(self, name, salary=50000, project=None):
        # Call the parent's constructor
        Employee.__init__(self, name, salary)

        # Assign project attribute
        self.project = project

    def display(self):
        print("Manager ", self.name)

m = Manager("King Grey", 10000000, "Winter Arc: Phase II")
m.display()