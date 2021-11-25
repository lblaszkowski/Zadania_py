numbers = str(input('Podaj liczby: '))

two_numbers = []

numeric_filter = filter(str.isdigit, numbers)
numeric_string = "".join(numeric_filter)

print(numeric_string)

for i in str(numeric_string):
    two_numbers.append(i)

print(two_numbers)