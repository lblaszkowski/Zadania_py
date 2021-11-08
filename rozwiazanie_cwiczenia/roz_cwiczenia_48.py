import random

liczba = int(input('Zgadnij jaka, to liczba: '))

for i in range(1):
    numbers = random.randint(1, 2)
    if liczba == numbers:
        print('Liczbę, która podał user, to {}, a wylosowana liczba, to {}' .format(liczba,numbers))
        print('User zgadł, jak to liczba został wylosowana. Gratulacje')
    else:
        print('Liczbę, która podał user, to {}, a wylosowana liczba, to {}' .format(liczba,numbers))
        print('User nie zgadł, jak to liczba został wylosowana. Przykro mi')
