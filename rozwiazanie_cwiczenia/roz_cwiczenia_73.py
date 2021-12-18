start = int(input("Podaj dolną granice liczbową: "))
stop = int(input("Podaj górną granice liczbową: "))
n = int(input("Liczbe podzielena: "))

### Przykład 1

# with open('../pliki/plik_73.text', 'w') as file:
#     for i in range(start, stop + 1):
#         if i % n == 0:
#             print(i, file=file, end=' ')
#             print(i, end=' ')
#     file.close()

### Przykład 2

with open('../pliki/plik_73.text', 'w') as file:
    for i in range(start, stop + 1):
        if i % n == 0:
            file.write(str(i) + ' ')
            print(i, end=' ')
    file.close()