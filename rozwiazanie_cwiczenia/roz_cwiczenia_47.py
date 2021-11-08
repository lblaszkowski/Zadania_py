import random

list_numbers = []
new_list_numbers = []

for i in range(10):
    numbers = random.randint(1, 50)
    list_numbers.append(numbers)

for a in list_numbers:
    if a > 10:
        new_list_numbers.append(a)

print('Pierwotna lista numerów ' + str(list_numbers))
print('Nowa lista numerów ' + str(new_list_numbers))