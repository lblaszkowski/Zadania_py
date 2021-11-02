parzyszte = []
nieparzyszte = []

for i in range(0, 100 + 1):
    if i > 0:
        if i % 2 == 0:
            parzyszte.append(i)
        else:
            nieparzyszte.append(i)

print('Liczby parzyszte = ' + str(parzyszte))
print('Liczby nieparzyszte = ' + str(nieparzyszte))