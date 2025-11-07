class Employee:
    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount


class Manager(Employee):
    def display(self):
        print("Manager ", self.name)

    def __init__(self, name, salary=50000, project=None):
        Employee.__init__(self, name, salary)
        self.project = project

    # Add a give_raise method
    def give_raise(self, amount, bonus=1.05):
        new_amount = amount * bonus
        Employee.give_raise(self, new_amount)


mngr = Manager("Ashta Dunbar", 78500)
mngr.give_raise(2000, bonus=1.03)
print(mngr.salary)

# alternatively using super()__init__()
# class Employee:
#     def __init__(self, name, salary=30000):
#         self.name = name
#         self.salary = salary
#
#     def give_raise(self, amount):
#         self.salary += amount
#
#
# class Manager(Employee):
#     def __init__(self, name, salary=50000, project=None):
#         # call parent constructor using super()
#         super().__init__(name, salary)
#         self.project = project
#
#     def give_raise(self, amount, bonus=1.05):
#         # calculate the raise including the bonus multiplier
#         new_amount = amount * bonus
#         # call the parent's give_raise using super()
#         super().give_raise(new_amount)
#
#
# # example run
# mngr = Manager("Ashta Dunbar", 78500)
# mngr.give_raise(2000, bonus=1.03)
# print(mngr.salary)   # expected: 78500 + (2000 * 1.03) = 80560.0
