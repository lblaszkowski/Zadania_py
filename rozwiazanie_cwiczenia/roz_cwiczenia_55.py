import random

list_numbers = []

for i in range(20):
    numbers = random.randint(1, 50)
    list_numbers.append(numbers)


max_list_numbers = max(list_numbers)
list_numbers.remove(max_list_numbers)
max_dwo_list_numbers = max(list_numbers)
print(max_dwo_list_numbers)