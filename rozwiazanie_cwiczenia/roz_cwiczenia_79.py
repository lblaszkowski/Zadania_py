#### Przykład 1

import random

list_numbers = []

for i in range(5):
    numbers = random.randint(1, 100)
    list_numbers.append(numbers)

now_list_numbers1, now_list_numbers2 = random.sample(list_numbers, 5), random.sample(list_numbers, 2)

x = len(now_list_numbers1)
y = len(now_list_numbers2)

if x >= y:
    print('Lista now_list_numbers1, ma elementów:', x
          ,' i jest wieksza od listy now_list_numbers2, która ma elementów:', y)
else:
    print('Lista now_list_numbers2, ma elementów:', y
          ,' i jest wieksza od listy now_list_numbers1, która ma elementów:', x)

#### Przykład 2
# import random
#
# list_numbers1 = []
# list_numbers2 = []
#
# for i in range(5):
#     numbers = random.randint(1, 100)
#     list_numbers1.append(numbers)
#
# for a in range(9):
#    numbers = random.randint(1, 100)
#    list_numbers2.append(numbers)
#
# print('lista 1', list_numbers1)
# print('lista 2', list_numbers2)


#### Przykład 3
import random

# a = []
# b = list(range(1, 20))

# for i in b:
#     t = random.randint(1, 10)
#     a.append(t)

# print('lista a', len(a), a)
# print('lista b', len(b), b)
