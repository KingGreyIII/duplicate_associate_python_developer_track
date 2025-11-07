class Player:
    MAX_POSITION = 10
    def __init__(self, position):
        if position <= Player.MAX_POSITION:
              self.position = position
        else:
              self.position = Player.MAX_POSITION
              
# Create Players p1 and p2
p1 = Player(9)
p2 = Player(5)

print("MAX_POSITION of p1 and p2 before assignment:")
# Print p1.MAX_POSITION and p2.MAX_POSITION
print(p1.MAX_POSITION)
print(p2.MAX_POSITION)

# Assign 7 to p1.MAX_POSITION
p1.MAX_POSITION = 7

print("MAX_POSITION of p1 and p2 after assignment:")
# Print p1.MAX_POSITION and p2.MAX_POSITION
print(p1.MAX_POSITION)
print(p2.MAX_POSITION)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_file(cls, filename):
        with open(filename, "r") as f:
            name = f.readline().strip()
            salary = f.readline().strip()
        return cls(name, salary)