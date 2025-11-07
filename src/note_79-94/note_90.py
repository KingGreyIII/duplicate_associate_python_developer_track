class Parent:
    def __eq__(self, other):
        print("Parent's __eq__() called")
        return True

class Child(Parent):
    def __eq__(self, other):
        print("Child's __eq__() called")
        return True

p = Parent()
c = Child()

print(c == p ,"\n")
print(p == p ,"\n")
print(c == c ,"\n")
print(p == c ,"\n")


