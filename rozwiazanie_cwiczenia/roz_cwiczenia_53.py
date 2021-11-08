import random

list_numbers = []

for i in range(20):
    numbers = random.randint(1, 50)
    list_numbers.append(numbers)

list_numbers_count = list_numbers.count(30)

print("Pierwotna lista liczb:  ", list_numbers)

if list_numbers_count > 0:
    print("Liczba 30 występuje na liście: ", list_numbers_count, 'raz(y)')
else:
	print("Liczba 30 nie występuje na liście: ", list_numbers_count, 'razy')