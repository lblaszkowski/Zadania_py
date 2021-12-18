import random

list_numbers = []

for i in range(5):
    numbers = random.randint(1, 50)
    list_numbers.append(numbers)


for x, y in enumerate(list_numbers):
    print('list_numbers [',x,']:', y, sep="", end=', ')

## przykład 2
# y = 0
# for x in list_numbers:
#     print('list_numbers [',y,']:', x, sep="", end=' ')
#     y += 1