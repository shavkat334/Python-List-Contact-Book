# Task 1
people = [("Ali", 24), ("Laylo", 30), ("Jasur", 19)]

eng_katta = people[0]

for odam in people:
    if odam[1] > eng_katta[1]:
        eng_katta = odam

print(eng_katta[0], "—", eng_katta[1], "yosh")