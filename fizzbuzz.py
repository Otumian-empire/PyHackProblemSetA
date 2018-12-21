# 8 - fizz buzz:
# write a function named fizzbuzz() that has one parameter named numrange.
# Imagine a series of a number from 1 to numrange.
# 1 2 3 4 5 6, ..., numrange
# Fizz and Buzz refer to any number that's a multiple of 3 and 5 respectively. In other words, if a number is divisible
# by 3, it is substituted with fizz; if a number is divisible by 5, it is substituted with buzz. If a number is simultaneously
# a multiple of 3 AND 5, the number is replaced with "fizz buzz." In essence, it emulates the famous children game
# "fizz buzz


def fizzbuzz(numrange):
    for i in range(1, numrange + 1):
        if (i % 3 == 0) and (i % 3 == 0):
            print("fizz buzz")
        elif (i % 3 == 0):
            print('fizz')
        elif (i % 5 == 0):
            print('buzz')
        else:
            print(i)

fizzbuzz(20)
