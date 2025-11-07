union_squirrels = ("Union Square Park", [
    {"primary_fur_color": "Gray", "activity": "Eating"},
    {"primary_fur_color": "Gray", "activity": "Running"},
    {"primary_fur_color": "Cinnamon", "activity": "Climbing"},
])

madison_squirrels = [
    {"primary_fur_color": "Gray", "activity": "Eating"},
    {"primary_fur_color": "Gray", "activity": "Sitting"},
    {"primary_fur_color": "Gray", "activity": "Jumping"},
]

# Step 1: create dictionary
squirrels_by_park = {}

# Step 2: add data
squirrels_by_park["Madison Square Park"] = madison_squirrels
squirrels_by_park.update([union_squirrels])

# Step 3: loop and print fur colours
# for park_name in squirrels_by_park:
#     fur_colors = [squirrel.get("primary_fur_color", "N/A")
#                   for squirrel in squirrels_by_park[park_name]]
#     print(park_name, fur_colors)

# Printing unique fur per park
"""My attempt with jst ref material"""
# unique_fur = {}
# for park_name in squirrels_by_park:
#     unique_fur = [squirrel["primary_fur_color"] for squirrel in squirrels_by_park[park_name]]
#     print(f"unique fur in {park_name} is {print(unique_fur)}")

# unique_fur = {}
# for park_name in squirrels_by_park:
#     # get all fur colours for this park
#     fur_colors = [squirrel["primary_fur_color"]
#                   for squirrel in squirrels_by_park[park_name]]
#     # keep only unique ones
#     unique_fur[park_name] = set(fur_colors)

# print results
# for park, furs in unique_fur.items():
#     # print(f"Unique fur in {park}: {furs}")
#     print("-" * 13)
# # print(type(unique_fur))
# gambit = {"ref", "cops", "eggs", "hang"}
# # print(gambit, type(gambit))

""""Attempt 3"""
# activity_tracker = {}
# counts = {}
# for park_name in squirrels_by_park:
#     activities = {}
#     for activity in squirrels_by_park[park_name]:
#         activities["activity"] = activities.get(activity,0) + 1
#         # fruit_counts[fruit] = fruit_counts.get(fruit, 0) + 1
print(squirrels_by_park)

"""AI generated for method 1 for qst 3"""
# counts = {}
# for park_name in squirrels_by_park:
#     activity_counter = {}
#     for activity in squirrels_by_park[park_name]:
#         activity_per_list = activity["activity"]
#         activity_counter[activity_per_list] = activity_counter.get(activity_per_list,0) + 1
#
#         counts[park_name] = [[activity, num] for activity, num in activity_counter.items()]
# print(counts)

"""task 3 method 2 attempt"""
activities ={}
for park_name in squirrels_by_park:
    for squirrel in squirrels_by_park[park_name]:
        activity_per_list = squirrel["activity"]
        activities[activity_per_list] = activities.get(activity_per_list,0) + 1
print(activities)

"""AI solution on activity 3 method 2"""
# activities = {}   # create once, outside the loop
#
# for park_name in squirrels_by_park:
#     for squirrel in squirrels_by_park[park_name]:
#         activity = squirrel["activity"]  # extract the string
#         activities[activity] = activities.get(activity, 0) + 1
#
# print(activities)

