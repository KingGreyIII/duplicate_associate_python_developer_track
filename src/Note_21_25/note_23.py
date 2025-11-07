first_ten = [(num ** 2) for num in range(1,11) if (num ** 2) < 20]
print(first_ten)

squirrels = [
    ("Central Park", ("Gray", "Eating")),
    ("Prospect Park", ("Cinnamon", None)),
    ("Riverside Park", ("Black", "Climbing"))
]
squirrel_detail = [content for content,detail in squirrels if len(content) > 10]
print(squirrel_detail)
