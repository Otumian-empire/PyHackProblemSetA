# 2 - Find all odd Fibonacci numbers starting from 3

def fib(n):
    if n > 1:
        return fib(n-1) + fib(n-2)
    else:
        return 1

# maximum recursion depth exceeded..  error
p = 1000
for i in range(p):
    if fib(i) % 2 == 1 and fib(i) >= 3:
        print(fib(i))
