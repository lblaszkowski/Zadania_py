import random

list_numbers = []

for i in range(20):
    numbers = random.randint(1, 100)
    list_numbers.append(numbers)

## przykład 1
print('Lista pierwotna ', list_numbers)
for i in list_numbers.copy():
    if i >= 10 and i <= 30:
        list_numbers.remove(i)
print('lista zmodyfikowana ', list_numbers)



## przykład 2
# list_numbers = [num for num in list_numbers if num < 10 or num > 30]
# print(list_numbers)

## przykład 3
# list_numbers = [num for num in list_numbers if num not in range(10, 30)]
# print(list_numbers)