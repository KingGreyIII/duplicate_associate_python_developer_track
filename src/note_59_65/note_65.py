import re
text = "I love the movie Avengers."

# Capturing group
cap = re.findall(r"(movie|concert)", text)

# Non-capturing group
noncap = re.findall(r"(?:movie|concert)", text)
noncapa = re.findall(r"(movie)", text)


print("Capturing:", cap)
print("Non-capturing:", noncap)
print(noncapa)
