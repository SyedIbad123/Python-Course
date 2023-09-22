# RECURSION IN PYTHON PROGRAMMING...
# 01 : The term Recursion can be defined as the process of defining something in terms of itself. In simple words, it is a process in which a function calls itself directly or indirectly..
# 02 : Recursion is a function calls itself..
# 03 : It is used to directly use of mathematical formula as a function..
# 04 : A complicated function can be split down into smaller sub-problems utilizing recursion.
# 05 : Sequence creation is simpler through recursion than utilizing any nested iteration.
# 06 : Recursive functions render the code look simple and effective.
# 07 : sometimes recursion is the most direct way to code an algorithm..

'''Disadvantages of using recursion
# 01 : A lot of memory and time is taken through recursive calls which makes it expensive for use.
# 02 : Recursive functions are challenging to debug.
# 03 : The reasoning behind recursion can sometimes be tough to think through.
# 04 : The programmer need to be extremly careful while using recursion to ensure that the function doesn't infinitely keep calling itself.
 '''
'''The syntax for recursion is..
          def func(): <--
                        |
                        | (recursive call)
                        |
              func() ----  '''
              


# Example no : 01 => Program to print factorial of n terms...

def recursive_factorial(n):
      if n == 1:
          return n
      else:
           return n * recursive_factorial(n-1)  # Here we use a mathematical formula for calculating factorial
 
# user input
num = int(input("Enter the number : "))
 
# check if the input is valid or not
if num < 0:
  print("Invalid input ! Please enter a positive number.")
elif num == 0:
  print("Factorial of number 0 is 1")
else:
  print("Factorial of number" , num , "=" , recursive_factorial(num))