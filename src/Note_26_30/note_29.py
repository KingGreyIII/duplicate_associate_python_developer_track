# Import namedtuple from collections
from collections import namedtuple
weight_log = [
    ('Gentoo', 'MALE', 5500.0), ('Chinstrap', 'MALE', 4300.0), ('Adlie', 'MALE', 3800.0), ('Gentoo', 'MALE', 5800.0), ('Chinstrap', 'MALE', 4100.0), ('Adlie', 'MALE', 3975.0), ('Gentoo', 'MALE', 5400.0), ('Chinstrap', 'MALE', 4800.0), ('Chinstrap', 'MALE', 3950.0), ('Gentoo', 'MALE', 5250.0), ('Gentoo', 'MALE', 4925.0), ('Adlie', 'MALE', 3950.0), ('Chinstrap', 'MALE', 3800.0), ('Chinstrap', 'MALE', 4050.0), ('Adlie', 'MALE', 3650.0)
]
# Create the namedtuple: SpeciesDetails
SpeciesDetails = namedtuple("SpeciesDetails", ['species', 'sex', 'body_mass'])

# Create the empty list: labeled_entries
labeled_entries = []

# Iterate over the weight_log entries
for species, sex, body_mass in weight_log:
    # Append a new SpeciesDetails namedtuple instance for each entry to labeled_entries
    labeled_entries.append(SpeciesDetails(species, sex, body_mass))

print(labeled_entries[:5])