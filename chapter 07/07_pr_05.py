# Program to find fictorial of a given number

num = int(input("Enter a number : "))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
print("The factorial of " ,i,"!= is " + str(factorial))




