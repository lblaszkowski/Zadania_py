print('Program do liczenia ilości godzin w danym roku')
rok = int(input('Podaj rok: '))

godzina = 24

if rok % 4 == 0 and rok % 100 != 0 or rok % 400 == 0:
    rokPrzestępnym = 366
    godzinyRoku = rokPrzestępnym * godzina
    print('Jest to rok', rok, 'i jest rokiem przestępnym. Ma 366 dni. Co daj nam ilości godzin:', godzinyRoku, 'w tym roku'  )

else:
    rokNieprzestępny = 365
    godzinyRoku = rokNieprzestępny * godzina
    print('Jest to rok', rok, 'i nie jest rokiem przestępnym. Ma 365 dni. Co daj nam ilości godzin:', godzinyRoku, 'w tym roku')

