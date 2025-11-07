weight_log = [('Chinstrap', 'FEMALE', 3800.0),
              ('Adlie', 'FEMALE', 3450.0),
              ('Gentoo', 'FEMALE', 4300.0),
              ('Adlie', 'FEMALE', 3550.0),
              ('Adlie', 'FEMALE', 3175.0)]

# Create an empty dictionary: female_penguin_weights
female_penguin_weights = {}

# Iterate over the weight_log entries
for species, sex, body_mass in weight_log:
    # Check to see if species is already in the dictionary
    if species not in female_penguin_weights:
        # Create an empty list for any missing species
        female_penguin_weights[species] = []
    # Append the sex and body_mass as a tuple to the species keys list
    female_penguin_weights[species].append((sex, body_mass))

# Print the weights for 'Adlie'
print(female_penguin_weights["Adlie"])


"""---------------section 2----------------------"""
# Import defaultdict
from collections import defaultdict

# Create a defaultdict with a default type of list: male_penguin_weights
male_penguin_weights = defaultdict(list)

# Iterate over the weight_log entries
for species, sex, body_mass in weight_log:
    # Use the species as the key, and append the body_mass to it
    male_penguin_weights[species].append(body_mass)

# Print the first 2 items of the male_penguin_weights dictionary
print(list(male_penguin_weights.items())[:2])