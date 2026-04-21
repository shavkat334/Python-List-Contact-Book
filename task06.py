# Task 6
emails = (
    ("Ali", "ali@gmail.com"),
    ("Vali", "vali@yandex.ru"),
    ("Sami", "sami@mail.ru")
)

domenlar = []

for user in emails:
    email = user[1]
    domen = email.split("@")[1]
    domenlar.append(domen)

print(domenlar)