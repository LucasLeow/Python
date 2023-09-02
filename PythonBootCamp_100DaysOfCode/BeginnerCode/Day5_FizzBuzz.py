# print Fizz if num divisible by 3
# print Buzz if num divisible by 5
# print FizzBuzz if num divisible by 3 & 5

for i in range(1, 100):
    if (i % 3 == 0 and i % 5 == 0):
        print(str(i) + " : " + "FizzBuzz")
    elif (i % 3 == 0):
        print(str(i) + " : " + "Fizz")
    elif (i % 5 == 0):
        print(str(i) + " : " + "Buzz")
    else:
        print(i)
