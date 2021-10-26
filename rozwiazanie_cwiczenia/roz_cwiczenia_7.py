rok = int(input('Podaj rok: '))

# rok = 2000

if rok % 4 == 0 and rok % 100 != 0 or rok % 400 == 0:
    print('Rok ' + str(rok) + ' jest rokiem przestępnym  i ma 366 dni')
else:
    print('Rok ' + str(rok) + ' nie jest rokiem przestępnym ma 365 dni')