# Task 4
orders = [(102, "Ali"), (99, "Vali"), (150, "Sami")]

juftlar = []

for order in orders:
    if order[0] % 2 == 0:
        juftlar.append(order)

print(juftlar)