import random

list_numbers = []
nieparzyste_numbers = []

for i in range(20):
    numbers = random.randint(1, 20)
    list_numbers.append(numbers)


for x in list_numbers:
    if x % 2 == 1:
        nieparzyste_numbers.append(x)

print("Pierwotna lista numerów:  ", list_numbers)
print("Liczby nieparzyste:  ", nieparzyste_numbers)
print("Suma liczb nieparzystych:  ", sum(nieparzyste_numbers))







