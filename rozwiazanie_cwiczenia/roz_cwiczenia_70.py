import random

list_numbers = []

for i in range(10):
    numbers = random.uniform(10.1, 30.12)
    new_numbers = round(numbers, 2)
    list_numbers.append(new_numbers)

print(list_numbers)


