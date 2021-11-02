liczba_startowa = int(input('Podaj początek liczby: '))
liczba_koncowa = int(input('Podaj koncową liczby: '))

for i in range(liczba_startowa, liczba_koncowa + 1):
    if i >= 10 and i <= 99:
        print(i)
