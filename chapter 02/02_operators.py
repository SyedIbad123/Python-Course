# OPERATORS IN PYTHON

# There are seven types of operator but we discuss here only four that is enough for our python basic.
 
# 01: ARITHMETIC OPERATORS : +,-,*,/,// ...
# 02: ASSIGNMENT OPERATORS : =,+=,-= ...
# 03: COMPARISON OPERATORS : ==,>,>=,<,!= ...  
# 04: LOGICAL OPERATORS : and, or ,not ...


# 01 : Arithmetic operators

a = 3
b = 4
print(" the value of 3+4 is", a+b)
print(" the value of 3-4 is", a-b)
print(" the value of 3*4 is", a*b)
print(" the value of 3*4 is", a**b) # double sterick(**) is used for x^y( x to the power y)
print(" the value of 3%4 is", a%b)  # Modulo operator is used to return remainder of division.
print(" the value of 3/4 is", a/b)
print(" the value of 3//4 is", a//b)  # double slash (//) is used for floor division(returns a real value and ignores the decimal part)


# 02 : Assignment operators

a = 34
a += 2 # this means a=a+2
a -= 2 # this means a=a-2
a *= 2 # this means a=a*2(multiply)
a /= 2 # this means a=a/2(divide)
a %= 2 # this means a=a%2(modulo)
a **= 2 # this means a=a**2(exponentiation)
a //= 2 # this means a=a//2(floor division)
print(a)

''' In python programming.. if any number is completeley divisible by any number than the output is floating point(only if we use simple divide operator not floor division operator)...'''


# 03 : Comparison operators
'''comparison operators prints in boolean variables '''

b = (4>6)
print(b)

b = (5==6)
print(b)


# 04 : logical operators

bool1 = True
bool2 = False
print("The value of bool1 and bool2 is ", (bool and bool2))
print("The value of bool1 or bool2 is ", (bool1 or bool2))
print("The value of not bool2 is ", ( not bool2)) # "not operator only used with one entity(value)..."


