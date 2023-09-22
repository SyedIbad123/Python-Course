# TRY WITH ELSE..
# 01 : Sometimes we want to run a piece of code  when try was successful. So, we use else statement..
# 02 : Else is only executed when your code is not iterate in except..

try:
    i = int(input("Enter a number : "))
    c = 1/i
except Exception as e :
    print(e)
else:
    print("We were successful!")
    
    