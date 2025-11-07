records = [
    ("Alice", "Math"),
    ("Alice", "Biology"),
    ("Bob", "Math"),
    ("Charlie", "History"),
    ("Bob", "History"),
]
"""Task:

Use defaultdict(list) to group subjects by student.

Print the grouped results, e.g. Alice: ['Math','Biology']."""

from collections import defaultdict
students_name = defaultdict(list)
for student_name, subject in records:
   students_name[student_name].append(subject)

for student_name, subject in students_name.items():
    print(f"{student_name} : {subject}")