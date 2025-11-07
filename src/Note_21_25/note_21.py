# # # Mini Project to reinforce knowledge on " "join.()
# # # 📝 Practice 1: Baby Names Formatter
# # #
# # # Task:
# # # You are given two lists: one with girl names and one with boy names.
# # #
# # # Pair them using zip().
# # #
# # # Loop through them with enumerate().
# # #
# # # Format each pair as "Rank X: GirlName & BoyName".
# # #
# # # Use " | ".join() to join all results into one string and print it.
# # # Example Output:
# # #
# # # Rank 1: Emma & Liam | Rank 2: Olivia & Noah | Rank 3: Sophia & Ethan
# # #
# # #
# # # What this tests:
# # #
# # # zip()
# # #
# # # enumerate()
# # #
# # # string formatting (f-strings)
# # #
# # # join() applied outside the loop.
"""Solution for task 1"""
girl_names = ["Emma", "Olivia", "Sophia", "Ava", "Mia"]
boy_names = ["Liam", "Noah", "Ethan", "Mason", "Logan"]
# names = zip(girl_names, boy_names)
# for rank, name in enumerate(names, start = 1):
#     girl_name, boy_name = name
#     line = ' | '.join([girl_name, boy_name])
#     print(f"Rank {rank}: {line}")
# """First task Completed"""

"""Second Task Commences"""
# # #📝 Practice 2: Top N Favourite Foods
# # #
# # #Task:
# # #You are given a list of 7 favourite foods.
# # #
# # #Slice the list to only get the top 5.
# # #
# # #Use a for loop to build a new list of strings: "Food #n: item".
# # #
# # #Use "\n".join() to print them each on a new line.
# # #
# # #Example Output:
# # #
# # #Food #1: Rice
# # #Food #2: Beans
# # #Food #3: Yam
# # #Food #4: Chicken
# # #Food #5: Pizza
# # #
# # #
# # #What this tests:
# # #
# # #list slicing
# # #
# # #for loop with enumerate(start=1)
# # #
# # #join() inside + outside the loop variations
# # #
# # #string formatting.
# """Solution for task 2"""
"""failed attempt"""
foods = ["Rice", "Beans", "Yam", "Chicken", "Pizza", "Pasta", "Burger"]
# for rank, food in enumerate(foods[:5], start = 1):
#     # item = [food]
#     bulk = f"The rank {rank} of the selected food {food}"
#     print(bulk)

""""New Task"""
# words = ["I", "love", "Python"]
# sentence = " ".join(words)
# print(sentence)
# for rank, (g, b) in enumerate(zip(girl_names, boy_names), start=1):
#     line = " - ".join([f"Rank {rank}:", g, b])
#     print(line)
for rank, (g, b) in enumerate(zip(girl_names, boy_names), start=1):
    # line = " - ".join([f"Rank {rank}:", g, b])
    # print(line)

    print(g + "\n" + b)


gonvit = {
    1 : "we",
    2 : "wrewe"
}
print(gonvit.values())