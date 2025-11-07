class Employee:
    def set_name(self, new_name):
        self.name = new_name

    # Add set_salary() method
    def set_salary(self, new_salary):
        self.salary = new_salary  # Ensure you're setting 'salary' here


emp = Employee()

# Use set_name to set the name of emp to 'Korel Rossi'
emp.set_name('Korel Rossi')

# Set the salary of emp to 50000
emp.set_salary(50000)  # Make sure the salary is set to 50000

# Print the emp object's salary

print(emp.salary)  # Ensure you're printing the 'salary' attribute