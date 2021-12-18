### Przykład 1
# s = input('Podaj dowolne 6 liczby po przecinku: ')
#
# a = s.split()
# print(a)


### Przykład 2
numbers = []
print('Podaj dowolne 6 liczb po przecinku: ')

for i in range(6):
    # i += 1
    s = input('Liczba numer {}: '.format(i + 1))
    numbers.append(s)

print(numbers)




