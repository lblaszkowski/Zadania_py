import heapq
import random

list_numbers = []

for i in range(20):
    numbers = random.randint(1, 50)
    list_numbers.append(numbers)


numbers_two = heapq.nlargest(2, list_numbers)

first_numbers = numbers_two[0]
second_numbers = numbers_two[1]

if first_numbers > second_numbers:
    print(first_numbers)
else:
    print(second_numbers)