# 3 - Write the a function to find the sum of the individual digits of a number and check whether 
# it's prime or not and whether it's even


def sum_of_digit(number):
    """ takes an int as a param and finds the sum of all the individual digits """
    total = 0

    if 0 <= number <= 9:
        total = number
    else:
        number = abs(number)
        number = list(str(number))
    
        for digit in number:
            total += int(digit)

    return total


def is_even(total):
    """ checks if a number is even and returns True, else False """
    total = abs(int(total))
    if total > 1 and total % 2 == 0:
        return True
    else:
        return False


def is_prime(n):
    """ checks if a number is prime and returns True, else False """
    flag = True

    if abs(n) <= 1:
        flag = False
    else:    
        for i in range(2, n):
            if n % i == 0:
                flag = False
        
    return flag


def indigprimeven(number):
    """ combines the three functions is_prime, sum_of_digit and is_even """
    sum_of_num = sum_of_digit(number)

    if is_prime(sum_of_num) == True and is_even(sum_of_num) == True:
        return ('sum of the individual digits of {} is {} and it is prime and even'.format(number, sum_of_num))
    elif is_prime(sum_of_num) == True and is_even(sum_of_num) == False:
        return ('sum of the individual digits of {} is {} and it prime but not even'.format(number, sum_of_num))
    elif is_prime(sum_of_num) == False and is_even(sum_of_num) == True:
        return ('sum of the individual digits of {} is {} and it is not prime but even'.format(number, sum_of_num))
    else:
        return ('sum of the individual digits of {} is {} and it is not prime and not even'.format(number, sum_of_num))




for i in range(100):
    print(i, indigprimeven(i))
