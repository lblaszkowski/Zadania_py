numbers = 100

for i in range(numbers + 1):
    if i % 15 == 0:
        print(str(i) + ' ' + ' FizzBuzz')
    elif i % 3 == 0:
        print(str(i) + ' ' + ' Fizz')
    elif i % 5 == 0:
        print(str(i) + ' ' + ' Buzz')
    else:
        print(i)