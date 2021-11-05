A = input('Podaj pierwszą z trzech liczb: ')
B = input('Podaj drugą z trzech liczb: ')
C = input('Podaj trzecią z trzech liczb: ')

if A >= B and A >= C:
    print('Najwieksza liczba to  ' + str(A))
elif B >= A and B >= C:
    print('Najwieksza liczba to  ' + str(B))
else:
    print('Najwieksza liczba to  ' + str(C))