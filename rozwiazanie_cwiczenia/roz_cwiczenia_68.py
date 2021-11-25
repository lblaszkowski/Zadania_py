import random

list_numbers = []

for i in range(20):
    numbers = random.randint(1, 100)
    list_numbers.append(numbers)

list_numbers_2 = list_numbers
print('Lista pierwotna ', list_numbers)

a = 0

for i in list_numbers:
    if i % 3 == 0 and i != 0:
        list_numbers_2.insert(a + 1, 0)
    a += 1
print('lista zmodyfikowana ', list_numbers_2)


## przykład 2
# nowa_lista = []
# for i in list_numbers:
#     nowa_lista.append(i)
#     if i % 3 == 0:
#         nowa_lista.append(0)
# print(nowa_lista)

