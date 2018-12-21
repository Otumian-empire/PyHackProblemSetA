# 6 - collatz:
# Write a function named collatz() that has one parameter named number. If number is even, then 
# collatz() should print number // 2 and return this value. If number is odd, then collatz() should print 
# and return 3 * number + 1.
# Then write a program that lets the user type in an integer and that keeps calling collatz() on that 
# number until the function returns the value 1. NB: // is floor division

def collatz(number):
    print(number)
    if number == 1:
        return number
    else:
        return_val = 0
        if number % 2 == 0:
            return_val = number // 2
            collatz(return_val)
        else:
            return_val = 3 * number + 1
            collatz(return_val)
            


userinput  = int(input('Enter an integer: '))
collatz(userinput)
