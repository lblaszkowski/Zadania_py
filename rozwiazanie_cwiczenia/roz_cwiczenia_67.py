list_numbers = [163, 29, 30, 7, 273, 44, 27, 259, 34, 0, 96, 215, 140, 59, 78, 274, 135, 31, 237, 117]

new_list_numbers = []

for i in list_numbers:
    if i >= 100:
        new_list_numbers.append(i)
        count = 0
        for elements in new_list_numbers:
            count += 1

print(list_numbers)
print('Ilość liczb 3-cyfrowych na liście jest: ', count)


