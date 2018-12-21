# 1 - Write a function that checks whether the individual digits of a 
# number is odd or even or zero

def digit_type(number):
    number = list(str(number))

    for digits in number:
        if int(digits) == 0:
            print(digits, "is zero")
        elif int(digits) % 2 == 0:
            print(digits, "is even")
        else:
            print(digits, "is odd")


digit_type(207324)
