float1 = float(0.0001)
float2 = float(0.00001)
float3 = float(0.0000001)
# Print floats 1, 2, and 3
print(float1)
print(float2)
print(float3)

# Print floats 2 and 3 using the f string formatter
print(f"{float2:f}")
print(f"{float3:f}")

# Print float 3 with a 7 f string precision
print(f"{float3:.7f}")

# Print the result of 2/1 and 1/2
print(2/1)
print(1/2)

# Print the floored division result of 2//1 and 1//2
print(2//1)
print(1/2)

# Print the type of 2/1 and 2//1
print(type(2/1))
print(type(2//1))

# Create an empty list
my_list = []

# Check the truthiness of my_list
print(bool(my_list))

# Append the string 'cookies' to my_list
my_list.append('cookies')

# Check the truthiness of my_list
print(bool(my_list))

# from collections import counter
from collections import Counter

data = ["apple", "apple", "banana"]
print(Counter(data))
