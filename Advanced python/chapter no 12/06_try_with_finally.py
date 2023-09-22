# TRY WITH FINALLY..
# 01 : Finally clause ensures execution of a piece of code irrespective of the exception.
# 02 : Finally is also executed when the program is exit.

try:
    i = int(input("Enter a number : "))
    c = 1/i
except Exception as e :
    print(e)
    exit()
finally:  
    print("We are done!") # This program is always executed.
    