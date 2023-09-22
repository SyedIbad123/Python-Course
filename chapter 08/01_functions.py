# FUNCTIONS IN PYTHON...
# 01 :  Functions are blocks of code or group of statements written to carry out a specified task.
# 02 : There are two types of functions in python:
#           User-Defined Functions - these types of functions are defined by the user to perform any specific task.
#           Built-in Functions - these type of functions are pre-defined in python. e.g: print(),len(),range() etc.
# 03 : Functions in python help the user to divide the program into smaller parts and solve them individually, thus making it easier to implement.
# 04 : Python functions help us to save the effort of rewriting the whole code. All we got to do is call the function once it is defined.
# 05 : Once a function is defined in python, it can be called as many times as needed, thus enhancing code reusability.
# 06 :  Since a large program is divided into sections with the help of functions, it helps in increasing the readability of code, at the same time ensuring easy debugging.
'''07 : The syntax for function in python
          def function_name():
           statements
            .
            . and so on..'''
# 08 : A function can accept some values it can work with.These values are called arguements. Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.Same arguements does'nt repeat inside a function it throws an error


# Example of function to add two numbers..

def my_sum(x,y):  # Here we give to it two arguements,but there is lot of arguements you can give.
    print("The sum of twwo numbers is", x+y)
my_sum(2,4) # This is calling a function(As we already saw it in point no: 04),(This returns tha value 6 after adding 2 and 4),(2 and 4 are arguements)


# Example No : 02
def my_percentage(marks):
    return (sum(marks)/550)*100   # Return statement is same as print statement, It is used with values.We use return statement with numbers most of the time..

marks = [89,90,93,79,80,85]     # Here we can assign marks in form of list, you can also use tuple.
percentage = my_percentage(marks)
print(percentage)


# A - Default parameters or arguements in python function...
# 01 : If we want to call the function without giving arguements we have to assign a default parameter in function under paranthesis...
# 02 : This value is used when no arguement is passed..

def my_name(name = "Student"):   # Here we are assign a name = "student" this means whenever any person calls the function without giving arguement in it the "stranger" prints out...
    print("WELCOME TO NED! " + name)
my_name("Ibad")
my_name() # Here there is no arguements so the default parameters will come in output...




