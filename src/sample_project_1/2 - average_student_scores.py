students_by_class = {
    "Class A": [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 70},
        {"name": "Grey", "score": 95},
        {"name": "Alpha", "score": 85},
        {"name": "Dregs", "score": 70},
        {"name": "Therga", "score": 100}
    ],
    "Class B": [
        {"name": "Charlie", "score": 88},
        {"name": "Dana", "score": 92},
        {"name": "Therga", "score": 20},
        {"name": "Alice", "score": 85},
        {"name": "Grey", "score": 10},
        {"name": "Winnie", "score": 95}
    ]
}
"""Task: Build a dict that shows the average score per student across all classes.
💡 Hint: You’ll need .get() with a list or tuple to track total and count, then divide at the end."""
# solution
"""First attempt but it wasn't what was requested"""
# average = {}
# total_score = []
#
# for student_class, student_details in students_by_class.items():
#     total_score = []
#     total_num = 0 #
#     for student_scores in student_details:
#         student_score = student_scores["score"]
#         total_score.append(student_score)
#     average[student_class] = sum(total_score)/len(total_score)
#
# print(average) #for average score per class

""""Second attempt"""
average = {}
grading = {}
for students_class, students_details in students_by_class.items():
    for student in students_details:
        student_name, student_score = student["name"], student["score"]
        if student_name not in grading:
            grading[student_name] = [0, 0]

        grading[student_name][0] += student_score
        grading[student_name][1] += 1

for student_name, (total, count) in grading.items():
    average[student_name] = total / count
print(average)
