dishes = ["Jollof", "Egusi", "Suya"]

tags = [["spicy", "rice"], ["soup", "leafy"], ["grilled", "meat"]]

dishes_tags = zip(dishes, tags)
for rank,(a,b) in enumerate(dishes_tags):
    meal = "-".join(b)
    print(meal)
#     # print(end_dish)
#     # print(type(dished))


# menu_lines = []
#
# for rank, (dish, tags_for_dish) in enumerate(zip(dishes, tags), start=1):
#     # join tags inside loop
#     joined_tags = "-".join(tags_for_dish)
#     # join the full line pieces
#     line = " ".join([str(rank) + ")", dish + ":", joined_tags])
#     menu_lines.append(line)
#
# # join outside loop with newline
# menu = "\n".join(menu_lines)
#
# print(menu)