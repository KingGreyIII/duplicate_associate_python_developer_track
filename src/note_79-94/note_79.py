# Create a Player class
class Player:
    # Create MAX_POSITION class attribute
    MAX_POSITION = 10

    # Add a constructor, setting position to zero
    def __init__(self, position):
        self.position = position


# Create a player p and print its MAX_POSITION
p = Player(12)
print(p.MAX_POSITION, p.position)

# or # Create a Player class
# class Player:
#
#   # Create MAX_POSITION class attribute
#   MAX_POSITION = 10
#
#   # Add a constructor, setting position to zero
#   def __init__(self,position = 0):
#     self.position = position
#
# # Create a player p and print its MAX_POSITION
# p = Player()
# print(p.MAX_POSITION)