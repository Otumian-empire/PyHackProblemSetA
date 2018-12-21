# 7 - comma-code:
# When given input as , spam = ['python', 'django', 'tensoflow', 'tkinter']
# Write a function that takes a list value as an argument and returns 
# a string with all the items separated by a comma and a space, with 
# and inserted before the last item. For example, passing the previous 
# spam list to the function would return 'python', 'django', 'tensoflow' and 'tkinter'.
# But your function should be able to work with any list value passed to it.



def comma_code(param, sep = ', '):
    
    if len(param) < 2:
        if len(param) == 0:
            print("The paramter list expected at least 1 argument but 0 found")
            return 
        else:
            print(param[0])
            return 
    else:
        for i in range(len(param)):
            if param[i] == param[-2]:
                sep = ''
                print(str(param[-2]) + " and ", end='')

            else:
                print(param[i] + sep, end='')
    print()


spam = ['python', 'django', 'tensoflow', 'tkinter']
for i in range(len(spam) + 1):
    comma_code(spam[:i])
    