# MATHS FUNCTION IN PYTHON...
# 01 : Math function is used to calculate math in easy way.
# 02 : These functions are fastest to calculate the math.
# 03 : For this we import here a module name (*math) for mathematical operations.

import math


# A - Ceil function
# 01 :  This function returns the smallest integral value greater than the number. If number is already integer, same number is returned...

a = 5.6
print("The ceil of 5.6 is : " , end="") # The end parameter is used to change the default behavior of print() statement in Python. That is, since print() automatically inserts a newline after each execution. Therefore, using end this can change. The end parameter is basically used to customized or sometime interactive output.
print(math.ceil(a))


# B - Floor function 
# 01 : This function returns the greatest integral value smaller than the number. If number is already integer, same number is returned. 
a = 5.6
print("The floor of 5.6 is : " , end="")
print(math.floor(a))   # This can also be done by using floor division(i.e: //) 


# C - Fabs function
# 01 : This function returns the absolute value of the number.

b = -3
print("The absolute value of b is : ", end="")
print(math.fabs(b))



# D - Factorial function
# 01 : This function returns the factorial of the number. An error message is displayed if number is not integral(positive). 
b = 3
print("The factorial value of b is : ", end="")
print(math.factorial(b))



# E - Copysign function
# 01 : This function returns the number with the value of ‘a’ but with the sign of ‘b’. The returned value is float type.
# 02 : In this function the first arguement is effected means the sign of first arguement is change only..
a = -10
b = 3
print("The copysign value of a and b is : ", end="")
print(math.copysign(a,b))   # In this function we can pass only two arguements



# F - Min and Max function
# 01 : As we know it by names, The min returns minimum value between two arguements and max returns maximumm value of two arguements..
a = 10
b = 20
print("The min value is " , end="")
print(min(a,b)) 

print("The max value is " , end="")
print(max(a,b)) 



# G - Pow function.
# 01 : The pow(x, y) function returns the value of x to the power of y (x^y)...
# 02 : Here the first arguement is base and second arguement is power..
a = 2
b = 3
print(pow(a,b)) 


# H - Sqrt function
# 01 : The sqrt() method returns the square root of a number.
# 02 : We can also find it by this method=> 4**0.5(this means the sqrt of 4)
a = int(input("Enter a number : "))
square_root = math.sqrt(a)
print("The square root of given number is : ", square_root)


# NOTE::: There are many and many more maths function in python but at basic level we first need to learn these..