# Task 2
students = [
    ("Ali", ["Fizika", "Matematika"]),
    ("Laylo", ["Ingliz tili"]),
    ("Jasur", ["Matematika", "Informatika"])
]

sanoq = 0

for student in students:
    if "Matematika" in student[1]:
        sanoq += 1

print(sanoq, "talaba Matematika fanini tanlagan.")