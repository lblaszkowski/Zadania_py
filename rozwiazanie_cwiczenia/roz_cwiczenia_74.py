with open('../pliki/plik_74_parzysta.text', 'w') as file1:
    with open('../pliki/plik_74_nieparzysta.text', 'w') as file2:
        for a in range(1, 100 + 1):
            if a % 2 == 0:
                file1.write(str(a) + ' ')
            else:
                file2.write(str(a) + ' ')
            print(a, end=' ')
    file2.close()
file1.close()