import random

list_numbers = []
numbers_two = []

for i in range(20):
    numbers = random.randint(1, 50)
    list_numbers.append(numbers)

for i in list_numbers:
    i = i * 2
    numbers_two.append(i)

print(list_numbers)
print(numbers_two)








