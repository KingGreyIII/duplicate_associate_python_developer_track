import re

# Example contract string
contract = "The contract was Signed on 12/25/2021."

# Try using a regex pattern that matches the date format
regex_dates = r"Signed\son\s(\d{2})/(\d{2})/(\d{4})"
dates = re.search(regex_dates, contract)

if dates:
    print("Month:", dates.group(1))
    print("Day:", dates.group(2))
    print("Year:", dates.group(3))