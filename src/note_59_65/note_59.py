tra = "0123456789"
rde = "123456789"

print(rde[2:8])

# Import datetime
from datetime import datetime

# Assign date to get_date
get_date = datetime.now()

# Add named placeholders with format specifiers
message = "Good morning. Today is {:%B %d, %Y}. It's {:%H:%M} ... time to work!"

# Use the format method replacing the placeholder with get_date

print(message.format(get_date,get_date))

nam = "Python"
print(f"my name is {nam !a}")
print(f"my name is {nam !s}")
print(f"my name is {nam !r}")