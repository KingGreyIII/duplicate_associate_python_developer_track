squirrels = [('Marcus Garvey Park', ('Black', 'Cinnamon', 'Cleaning', None)), ('Highbridge Park', ('Gray', 'Cinnamon', 'Running, Eating', 'Runs From, watches us in short tree')), ('Madison Square Park', ('Gray', None, 'Foraging', 'Indifferent')), ('City Hall Park', ('Gray', 'Cinnamon', 'Eating', 'Approaches')), ('J. Hood Wright Park', ('Gray', 'White', 'Running', 'Indifferent')), ('Seward Park', ('Gray', 'Cinnamon', 'Eating', 'Indifferent')), ('Union Square Park', ('Gray', 'Black', 'Climbing', None)), ('Tompkins Square Park', ('Gray', 'Gray', 'Lounging', 'Approaches'))]

squirrels_by_park = {}
for park, squirrel_details in squirrels:

    line = " / ".join(str(detail) for detail in squirrel_details) # give this error line = " / ".join(squirrel_details)
# TypeError: sequence item 3: expected str instance, NoneType found
    squirrels_by_park[park] = line
""""On a side note, does the fact that it isnt in enumerate switch up from the previous one i have been learning when using \" \".join(list/tuple) """
    # squirrels_by_park[park] = list(line)
print(squirrels_by_park)

# for park in sorted(squirrels_by_park):
#
#     # line = "/".join(details_1)
#     print(f"{park}: {squirrels_by_park[park]}")
    # print(type(squirrels_by_park[park]))
    # print(print(True) if squirrels_by_park[park] == squirrel_details)
"""didnt get it ,but this waht i tried, left some extras to give an idea of the build , and pattern i tried to get it to work"""