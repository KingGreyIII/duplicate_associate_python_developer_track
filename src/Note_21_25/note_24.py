# --- Step 1: Setup data ---

# A dictionary that maps park names to a list of squirrels (each squirrel = dict of attributes)
squirrels_by_park = {
    "Central Park": [
        {"primary_fur_color": "Gray", "activity": "Eating"},
        {"primary_fur_color": "Cinnamon", "activity": "Running"}
    ],
    "Prospect Park": [
        {"primary_fur_color": "Black", "activity": "Climbing"}
    ]
}

# New squirrel list for Madison Square Park
squirrels_madison = [
    {"primary_fur_color": "Gray", "activity": "Sleeping"},
    {"primary_fur_color": "Cinnamon", "activity": "Eating"}
]

# Tuple for Union Square Park (note how it’s structured for .update)
squirrels_union = (
    "Union Square Park",
    [
        {"primary_fur_color": "Black", "activity": "Running"},
        {"primary_fur_color": "Gray", "activity": "Climbing"}
    ]
)


# --- Step 2: Apply the instructions ---

# Assign squirrels_madison as the value to the 'Madison Square Park' key
squirrels_by_park['Madison Square Park'] = squirrels_madison

# Update squirrels_by_park with the squirrels_union tuple
squirrels_by_park.update([squirrels_union])

# --- Step 3: Loop and safely extract colours ---
for park_name in squirrels_by_park:
    # For each squirrel in the list for this park, get 'primary_fur_color' safely
    fur_colors = [squirrel.get("primary_fur_color", "N/A")
                  for squirrel in squirrels_by_park[park_name]]
    print(park_name, fur_colors)
