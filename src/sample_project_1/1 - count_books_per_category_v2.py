library = {
    "Fiction": [
        {"title": "Book A", "author": "Alice", "copies": 3},
        {"title": "Book B", "author": "Bob", "copies": 1},
        {"title": "Book A", "author": "Alice", "copies": 2}
    ],
    "Science": [
        {"title": "Book C", "author": "Carol", "copies": 1},
        {"title": "Book D", "author": "Dan", "copies": 4}
    ]
}

"""Task: For each category (key), count how many times each book appears.
💡 Hint: Similar to your activity_counter logic, but run it for each category."""
# solution
book_counts ={}
for category, values in library.items():
    count = {}
    for book in values:
        book_name = book["title"]
        count[book_name] = count.get(book_name, 0) + 1
    book_counts[category] = count
print(book_counts)

"""method 2"""
book_counts_global = {}
for category, values in library.items():
    for value in values:
        book_title =value["title"]
        book_counts_global[book_title] = book_counts_global.get(book_title, 0) + 1
print(book_counts_global)

"""AI Correction"""

# Method 1: Count per category
"""category_counts = {}
for category, books in library.items():
    counts = {}
    for book in books:
        title = book["title"]
        counts[title] = counts.get(title, 0) + 1
    category_counts[category] = counts

print("Counts per category:", category_counts)"""


# Method 2: Count globally across all categories
"""global_counts = {}
for books in library.values():
    for book in books:
        title = book["title"]
        global_counts[title] = global_counts.get(title, 0) + 1

print("Global counts:", global_counts)"""