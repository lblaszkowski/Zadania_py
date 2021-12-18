list = [0, 2, 4, 5, 0, -1, 0, 6]
list_now = []

for i in list:
    list_now.append(i)
    if i == 4:
        list_now.append(i)
print(list_now)