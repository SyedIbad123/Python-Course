# CONDITIONAL EXPRESSION.

# A - If else and elif statements...
# if else and elif statements are a  multiway decision taken by our program due to certian condition in our code..
# else is optional in if-elif ladder...(important)

# Syntax:
''' if (condition):             
        print("yes)     # if condition 1 is tue...
        
    elif(conditon 2):
        print("no)      # if codition 2 is true...
           
    else:               # in else statement tere is no condition given... 
        print("maybe)   # otherwise

 '''
    
    
    
# 01 : if-elif-else ladder
# In this ladder code will execute always first statement which is true for given value..

# a = 21

# if (a<3):
#     print(" the value of a is greater than 3")
    
# elif(a<9):
#     print("the value of a is greater than 9")
    
# elif(a>20):
#     print("the value of a is greater than 20")

# else:
#     print("the value of a is less")
    
    
    
    
# 02 : Multiple if statements...
# In multiple if statements the code will execute if more than one statement is true...
    
a = 19

if (a<3):
    print(" the value of a is greater than 3")
    
if(a>9):
    print("the value of a is greater than 9")
    
if(a>20):
    print("the value of a is greater than 20")
else:
    print("the value of a is less than 20")
    
    
age = int(input("Enter your age"))
if age>=18:
    print("yes")
else:
    print("no")