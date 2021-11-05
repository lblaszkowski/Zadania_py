k = 3

for i in range(0, 15 + 1):
    if i > 0:
        if i % k ==0:
            print(str(i) + ' liczba jest podzielna przez ' + str(k))
        else:
            print(str(i) + ' liczba nie jest podzielna przez ' + str(k))
