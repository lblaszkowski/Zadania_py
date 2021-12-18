list = [0, 2, 4, 5, 0, -1, 0, 6]

for i in list:
    if i == 0:
        list.append(list.pop(list.index(0)))
print(list)

