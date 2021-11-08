import random

list_numbers = []
nieparzyste_numbers = []

for i in range(20):
    numbers = random.randint(1, 20)
    list_numbers.append(numbers)


for i in list_numbers:
    nieparzyste_numbers.append(i ** 2)

print("Pierwotna lista liczb:  ", list_numbers)
print("Liczby podniesione do kwadratu:  ", nieparzyste_numbers)

