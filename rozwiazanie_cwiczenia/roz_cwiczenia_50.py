import random

list_numbers = []
parzyste_numbers = []

for i in range(20):
    numbers = random.randint(1, 50)
    list_numbers.append(numbers)


for x in list_numbers:
    if x % 2 == 0:
        parzyste_numbers.append(x)
print("Pierwotna lista numerów:  ", list_numbers)
print("Liczby parzyste:  ", parzyste_numbers)
print("Suma liczb parzystych:  ", sum(parzyste_numbers))







