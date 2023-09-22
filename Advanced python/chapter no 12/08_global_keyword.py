# GLOBAL KEYWORD..
# 01 : A global keyword is a keyword that allows a user to modify a variable outside the current scope.
# 02 : Global keyword is used inside a function only when we want to do assignments or when we want to change a variable.

# RULES OF GLOBAL KEYWORD:
# 01 : If a variable is assigned a value anywhere within the function’s body, it’s assumed to be a local unless explicitly declared as global.
# 02 : Variables that are only referenced inside a function are implicitly global.
# 03 : We use a global keyword to use a global variable inside a function.
# 04 : There is no need to use global keywords outside a function.


# EXAMPLE NO : 01

a = 10           # Global variable
def my_func():
    global a # Here global keyword is used to change the global variable.
    a = 20   # Local variable if global keyword is not used.
    print(a)
my_func()
print(a)