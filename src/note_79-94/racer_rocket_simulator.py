# class Racer:
#     MAX_POSITION = 100
#
#     def __init__(self, name, speed = 10, position = 0):
#         self.name = name
#         self.speed = speed
#         self.position = position
#
#     def move(self, steps = 5):
#         if self.position + self.speed < self.MAX_POSITION:
#             self.position += self.speed
#         else:
#             self.position = self.MAX_POSITION
#
# class Rocket(Racer):
#     MAX_POSITION = 300
#
#     def __init__(self, fuel = 100):
#         self.fuel = fuel
#
#     def move(self, steps):
#         self.fuel -= 10
#
#         if self.fuel > 0:
#             self.speed *= 2
#         else:
#             print("Rocket is out of Fuel")
#
# racer = Racer("Falcon")
# rocket = Rocket("StarFire", speed = 25)
# racer.move()
# rocket.move()
# rocket.move()
# print(racer.position)
# print(rocket.position)
# print(rocket.fuel)

# AI solution
class Racer:
    MAX_POSITION = 100

    def __init__(self, name, speed=10, position=0):
        self.name = name
        self.speed = speed
        self.position = position

    def move(self):
        if self.position + self.speed < self.MAX_POSITION:
            self.position += self.speed
        else:
            self.position = self.MAX_POSITION


class Rocket(Racer):
    MAX_POSITION = 300

    def __init__(self, name, speed=20, position=0, fuel=100):
        # call the Racer constructor to handle name, speed, and position
        super().__init__(name, speed, position)
        self.fuel = fuel

    def move(self):
        if self.fuel <= 0:
            print(f"{self.name} is out of fuel!")
            return

        move_distance = self.speed * 2
        self.fuel -= 10

        if self.position + move_distance < self.MAX_POSITION:
            self.position += move_distance
        else:
            self.position = self.MAX_POSITION

        print(f"{self.name} zoomed to position {self.position}! Remaining fuel: {self.fuel}")


# Create the objects
racer = Racer("Falcon")
rocket = Rocket("StarFire", speed=25)

# Simulate movement
racer.move()
rocket.move()
rocket.move()

# Print final states
print(racer.position)
print(rocket.position)
print(rocket.fuel)
