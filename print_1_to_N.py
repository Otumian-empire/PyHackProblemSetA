# 5 - print from 1 to N:
# When input = 5
# output = 1,2,3,4,5
# When input = 9
# output = 1,2,3,4,...,9

N = int(input('Enter a number: '))
for i in range(1, N +1):
    if i == N:
        print(i)
    else:
        print(i, end=', ')
