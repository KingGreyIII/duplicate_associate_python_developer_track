import re

cellphones = [
    "123-4567-890123",
    "123-4567-890123-45",
    "987-6543-210987"
]

for phone in cellphones:
    # Try using a negative lookahead to exclude numbers followed by an extension
    number = re.findall(r"\d{3}-\d{4}-\d{6}(?!-\d{2})", phone)
    print(number)