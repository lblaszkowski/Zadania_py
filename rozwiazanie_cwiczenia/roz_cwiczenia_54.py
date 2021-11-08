import random

list_numbers = []
sum_list_numbers = []

for i in range(20):
    numbers = random.randint(1, 50)
    list_numbers.append(numbers)


for i in range(len(list_numbers)-1):
    sum_list_numbers.append(list_numbers[i] + list_numbers[i+1])

print('Największa suma elementów, to: ', max(sum_list_numbers))






