for i in range(1, 100 + 1):
    if i > 1:
        for a in range(2, i):
            if i % a == 0:
                break
        else:
            print(i)
    elif i == 0 or i == 1:
        print(i, "Podane liczby, to nie liczby pierwsze/a")
    else:
        print(i, "Podane liczby, to nie liczby pierwsze/a, a liczby/a złożone/a")