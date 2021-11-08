list_numbers = [98, 54, 67, 39, 75, 1, 24, 45, 76, 27, 42, 73, 56, 61, 87, 85, 79, 32, 3, 81, 19,
                48, 18, 16, 99, 52, 42, 18, 92, 93]

print(len(list_numbers))

for i in list_numbers:
    if i == 24 or i == 92 or i == 73 or i == 61 or i == 56 or i == 3 or i == 98 and i == 1:
        list_numbers.remove(i)

print(len(list_numbers))