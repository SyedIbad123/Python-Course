# For loop

# 01 : It's works as same as the while loop..
# 02 : This is fastest..
# 03 : For loop is used to iterate through a sequence like tuples,sets,dict,list e.t.c...
''' 04 : The syntax of for loop is =>
            for (control variable) in variable:  #(semicolon is mendatory)
                ---code---...
'''

# Print list by using for loop...

Random = ["ali", "cricket", "mangoes", "flowers"]
for item in Random:
    print(item)
    
    

# A - Range function
# 01 : The range function of python is used to generate a sequence of numbers..
# 02 : It always take integer as an arguement..
# 03 : range(arg1,arg2,arg3).... arg1 = starting number...arg2 = stoping number...arg3 = step-size..

for i in range(8):  
    print(i)

for i in range(4,6):  # it prints the numbers (4 to 5),always returns (n-1).
    print(i)
    
for i in range(2,10,2):
    print(i)



# B - Else in For loop..
# 01 : An optional else can be used with a for loop if the code is to be executed when the loop exhausts..
# 02 : It is only executable when loop condition is false...
# 03 : It's only execute on the successful termination on for loop...

for i in range(10):
    print(i)
else:
    print("I am IBAD")


# C - The break statement
# 01 : It is used to come out with the loop when encountered..
# 02 : It instruct the program to exit immediately..

for i in range(10):
    print(i)
    if i == 6:
        break
    
    
    
# D - Continue statement
# 01 : It is used to stop current iteration of the loop and continue with the next one.
# 02 : It instruct a program to "skip this iteration"...

for i in range(10):
    if i == 6:
        continue     # This statement current iteration means the value of 6 is skipped..
    print(i)



# Program to print the odd numbers using continue statement...

for i in range(10):
    if i % 2 == 0 :   # This skips current iteration means even numbers, So it prints odd numbers..
        continue     
    print(i)



# program to print the even numbers using continue statement....

for i in range(10):
    if i % 2 != 0 :    # This skips current iteration means even numbers, So it prints odd numbers..
        continue
    print(i)


# E - Pass statement
# 01 : It is a null statement in python.
# 02 : It instructs he program to do nothing..
# 03 : It can be used with conditional statements,loops,functions,objects e.t.c...
# 04 : It is also used to left blank spaces in program when we are don't write a code at particular time...

i = 0
if i<0:
    pass         # If we doesn't write pass, program will throw an error..
print("Ibad")