import random

losowanie = []

i = 1

while i <= 10:
    x = random.randint(1, 1000)
    if losowanie.count(x) == 0:
        losowanie.append(x)
        i += 1

print(losowanie)

