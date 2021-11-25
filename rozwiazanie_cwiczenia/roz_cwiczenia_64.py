import random

list_numbers = []

for i in range(5):
    numbers = random.randint(1, 50)
    list_numbers.append(numbers)

y = 0
for x in list_numbers:
     print(f"list_numbers[{y}]: {x}")
     y += 1

### Przykład 2
# for x, y in enumerate(list_numbers):
#     print('list_numbers[{}]:{}' .format(y, x))


### Przykład 3
# for x, y in enumerate(list_numbers):
#     print('list_numbers [',x,']:', y, sep="")


### Przykład 4
### Jak chcemy mieć spacje w indeksach
# y = 0
# for x in list_numbers:
#     print('list_numbers [',y,']:', x )
#     y += 1


