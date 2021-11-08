import random

list_numbers = []

for i in range(20):
    numbers = random.randint(1, 50)
    list_numbers.append(numbers)

list_numbers_max = max(list_numbers, key=list_numbers.count)
list_numbers_countt = list_numbers.count(list_numbers_max)

print(list_numbers)
print('Liczba {} występuje: {} raz(y)' .format(list_numbers_max, list_numbers_countt))