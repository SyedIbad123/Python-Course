# HANDLING DIFFERENT EXCEPTIONS...



# Value Error handling..
try:
    a = int(input("Enter a number :"))
    b = 1/a
    print(b)
except ValueError as e :
    print("Please enter a valid value")
print("Thanks!")



# Zero division error handling...
try:
    a = int(input("Enter a number :"))
    b = 1/a
    print(b)
except ZeroDivisionError as e :
    print("excption occured")
print("Thanks!")

