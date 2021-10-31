numbers = 50

FizzBuzz = []
not_FizzBuzz = []

for i in range(numbers + 1):
    if i > 0:
        if i % 15 == 0:
            FizzBuzz.append(str(i) + ' FizzBuzz')
        elif i % 3 == 0:
            FizzBuzz.append(str(i) + ' Fizz')
        elif i % 5 == 0:
            FizzBuzz.append(str(i) + ' Buzz')
        else:
            not_FizzBuzz.append(i)


print(FizzBuzz)
print(not_FizzBuzz)