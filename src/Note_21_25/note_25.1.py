baskets = {
    "BasketA": ["apple", "orange", "apple", "banana", "grape", "peanut", "peanut", "raspberry"],
    "BasketB": ["apple", "apple", "orange"]
}

counts = {}
for basket_name in baskets:
    # step 1: temporary dict for counting
    fruit_counts = {}
    for fruit in baskets[basket_name]:
        # step 2: increment count
        fruit_counts[fruit] = fruit_counts.get(fruit, 0) + 1

    # step 3: convert dict to list-of-lists
    counts[basket_name] = [[fruit, num] for fruit, num in fruit_counts.items()]

print(counts)
# Output: {'BasketA': [['apple', 2], ['orange', 1], ['banana', 1]],
#          'BasketB': [['apple', 2], ['orange', 1]]}
