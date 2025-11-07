# girl_names = ["Emma", "Olivia", "Sophia"]
# boy_names = ["Liam", "Noah", "Ethan"]
#
# pairs = zip(girl_names, boy_names)
# # print(next(names))
# for idx, pair in enumerate(pairs, start = 1):
#     girl_name, boy_name = pair
#     print(f"Rank {idx} : {girl_name} and {boy_name}")

# # # or

girl_names = ["Emma", "Olivia", "Sophia"]
boy_names = ["Liam", "Noah", "Ethan"]

pairs = zip(girl_names, boy_names)

# One-liner: build a list of formatted strings
ranked_pairs = [f"Rank {idx}: {girl} and {boy}"
                for idx, (girl, boy) in enumerate(pairs, start=1)]

print(ranked_pairs)
print("\n".join(ranked_pairs))

