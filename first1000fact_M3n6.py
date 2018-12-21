# 10 - Find the first 1000 factorial numbers that are both multiples of 3 and 6


def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)


# created to variables, one to return the factorial which is a multiple of 3 and 6, fact_number
# if the result is not, aux_number is incremented by 1
fact_number = aux_number = 0

while True:
    if fact_number == 1000:
        break
    elif (fact(fact_number + aux_number) % 3 == 0) and (fact(fact_number + aux_number) % 6 == 0):
        print(fact(fact_number + aux_number))
        fact_number += 1
    else:
        aux_number += 1
