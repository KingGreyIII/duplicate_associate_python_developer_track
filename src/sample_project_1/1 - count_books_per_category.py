library = {
    "Fiction": ["Book A", "Book B", "Book A", "Book C"],
    "Science": ["Book D", "Book E", "Book D"],
    "History": ["Book F", "Book F", "Book G"]
}
"""Task: For each category (key), count how many times each book appears.
💡 Hint: Similar to your activity_counter logic, but run it for each category."""
# solution
book_count = {}
for genre in library: #to get the keys
    count = {}
    for book in library[genre]: # to get the value of the keys
       count[book] = count.get(book, 0) + 1
    book_count[genre] = [[name,num] for name,num in count.items()]
    # book_count[genre] = [num for name,num in count.items()]
    # print(count.keys())
print(book_count)

"""The above is for method 1"""
"""Attempting with the genre grouping """
book_count_2 = {}
for genre in library:
    for category in library[genre]:
        book_count_2[category] = book_count_2.get(category, 0) + 1
    print(book_count_2)


"""AI correction"""

"""book_count = {}

for genre, books in library.items():
    count = {}
    for book in books:
        count[book] = count.get(book, 0) + 1
    book_count[genre] = count   # keep it as a dict for clarity

print(book_count)"""

"""📌 Output:{
  'Fiction': {'Book A': 2, 'Book B': 1, 'Book C': 1},
  'Science': {'Book D': 2, 'Book E': 1},
  'History': {'Book F': 2, 'Book G': 1}
}"""

"""🟢 Method 2 — Count across all genres (flattened)
book_count_global = {}

for books in library.values():
    for book in books:
        book_count_global[book] = book_count_global.get(book, 0) + 1

print(book_count_global)
"""

"""📌 Output:

{
  'Book A': 2,
  'Book B': 1,
  'Book C': 1,
  'Book D': 2,
  'Book E': 1,
  'Book F': 2,
  'Book G': 1
}"""