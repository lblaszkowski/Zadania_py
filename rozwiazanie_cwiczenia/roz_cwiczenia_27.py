import time

liczba = int(input('Podaj liczbe: '))

for i in range(liczba):
    i +=1
    time.sleep(2)
    print(i)
