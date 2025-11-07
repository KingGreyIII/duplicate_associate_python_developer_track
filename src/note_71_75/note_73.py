class Employee:

    # Include a set_name method
    def set_name(self, new_name):
        self.name = new_name


emp = Employee()

# Use set_name() on emp to set the name of emp to 'Korel Rossi'
emp.set_name('Korel Rossi')
print(emp.name)