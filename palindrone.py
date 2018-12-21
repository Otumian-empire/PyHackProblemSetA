# 4 - Write a function that checks whether some digits is a palindrome or not. Single digits are omitted

def is_palindrome(digit):

    # reversing digit
    new_digit  = list(str(digit))
    new_digit.reverse()
    new_digit = ''.join(new_digit)

    palin = False
    
    if len(str(digit)) > 1  and str(digit) == new_digit:
        palin = True
    else:
        palin = False
    
    return palin


for i in range(10, 100):
    print(i, is_palindrome(i))
