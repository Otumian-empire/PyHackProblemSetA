# 9 - Write a function that when given a digit it reverses it
# when input = 1234
# output = 4321

def reverse_digit(digit):
    """ To use the value from this function you must cast the return value """
    digit = list(str(digit))
    digit.reverse()
    digit = ''.join(digit)

    return digit

for i in range(1, 1000, 30):
    print(i, reverse_digit(i))
