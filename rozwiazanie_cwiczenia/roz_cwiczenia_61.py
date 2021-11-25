import random

list = []

for i in range(20):
    r = random.randint(1, 100)
    if r not in list:
        list.append(r)
print(list)
