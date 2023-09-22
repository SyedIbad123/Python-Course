# TRY STATEMENT..
# 01 : When an error occurs, or exception as we call it, Python will normally stop and generate an error message.These exceptions can be handled using the try statement
# 02 : The try block lets you test a block of code for errors.
'''The syntax is :
       try: 
        code here...'''
# 03 : First, the try clause is executed i.e. the code between try and except clause.
# 04 : If there is no exception, then only the try clause will run, except the clause is finished.
# 05 : If any exception occurs, the try clause will be skipped and except clause will run.
# 06 : If any exception occurs, but the except clause within the code doesn’t handle it, it is passed on to the outer try statements. If the exception is left unhandled, then the execution stops.
# 07 : A try statement can have more than one except clause.





# EXCEPT STATEMENT...
# 01 : The except block lets you handle the error.
# 02 : The code of except block is only executed if an exception occured in the try block. 
# 03 : The except block is required with a try block, even if it contains only the pass statement.


# Example no : 01
# try:
#  print(x)      # This throws an error of variable is not defined..
# except:
#   print("An exception occurred")



# # Example no : 02 
try:
    x = int(input("Enter a number"))
    y = int(input("Enter a number"))
    print("The result of your division is :", x/y)
except:
    print("Please enter a positive integer in denominator !")
    

# Example no : 03

try:
  num = int(input("Enter number: "))        
  print(num + 1)
except:
    print("Invalid Input")


        
# Example no : 04

while(True):
    print("press q to quit")
    a = input("Enter a  number : ")
    if a == "q":
        break
    try: 
        print("Trying...")
        a = int(a)
        if a>10:
            print("The number is greater than 10 ")
    except Exception as e:
        print(f"Your input resulted in an error : {e}")
        
print("Thanks ! ")


