import random

number = []

for i in range(20):
    numbers = random.randint(1, 100)
    number.append(numbers)

print(number)
with open('../pliki/plik_72.text', 'w') as file:
    for line in number:
        file.writelines(' '.join(str(line)))
    file.close()