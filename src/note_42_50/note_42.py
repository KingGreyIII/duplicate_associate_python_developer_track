import pandas as pd

# Step 1: Load the data
def load_data():
    """Simulate loading data like in the DataCamp example"""
    data = pd.DataFrame({
        'height': [72.1, 69.8, 63.2, 64.7],
        'weight': [198, 204, 164, 238]
    })
    return data

# Step 2: Functions to apply
def mean(data):
    """Return column means"""
    return data.mean()

def std(data):
    """Return column standard deviations"""
    return data.std()

def minimum(data):
    """Return column minimums"""
    return data.min()

def maximum(data):
    """Return column maximums"""
    return data.max()

# Step 3: Create the function map
function_map = {
    'mean': mean,
    'std': std,
    'minimum': minimum,
    'maximum': maximum
}

# Step 4: Simulate DataCamp behaviour
data = load_data()
print(data)
func_name = input("Type a command:\n> ").strip()  # e.g. "minimum"

# Step 5: Apply the chosen function
if func_name in function_map:
    result = function_map[func_name](data)
    print(result)
else:
    print(f"Unknown command '{func_name}'. Try one of: {list(function_map.keys())}")



# def mean(x): return sum(x) / len(x)
# def std(x): return (sum((i - mean(x))**2 for i in x) / len(x))**0.5
#
# function_map = {
#     'mean': mean,
#     'std': std,
#     'minimum': min,
#     'maximum': max
# }
#
# data = [4, 6, 8, 10, 12]
#
# func_name = input("Enter a function (mean, std, minimum, maximum): ")
#
# if func_name in function_map:
#     print("Result:", function_map[func_name](data))
# else:
#     print("Invalid choice.")
