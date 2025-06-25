students = [
    {"name": "Sai", "grade": 82},
    {"name": "Bhasker", "grade": 68},
    {"name": "Madhu", "grade": 91},
    {"name": "Takkum", "grade": 74},
    {"name": "pramod", "grade": 79}
]

# Print names of students with grade > 75
print("Students with grade > 75:")
for student in students:
    if student["grade"] > 75:
        print(student["name"])
