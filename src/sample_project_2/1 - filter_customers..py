customers = [
    {
        "name": "Alice",
        "email": "alice@example.com"
    },
    {"name": "Bob", "email": ""},
    {"name": "Charlie", "email": None},
    {"name": "Diana", "email": "diana@example.com"},
]
"""Task:

Loop through customers and filter out those without a valid email (use truthy/falsy).

Print the names of valid customers.

Hint: An empty string "" and None are falsy."""
# solution
name = []
for dict in customers:
    if bool(dict["email"]):
        name.append(dict["name"])
print(name)

"""AI solution"""
# Pythonic solution using list comprehension and truthiness
valid_names = [customer["name"] for customer in customers if customer["email"]]

print(valid_names)