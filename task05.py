# Task 5
numbers = (3, 6, 7, 8, 10, 11)

juft_sonlar = []

for son in numbers:
    if son % 2 == 0:
        juft_sonlar.append(son)

print(tuple(juft_sonlar))