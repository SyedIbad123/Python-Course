# program to find an average of two numbers entered by a user

a = input("Enter a first number : ")
b = input("Enter a second number : ")
a = int(a) # We can change it into an integer bcz input function stores data in atrings
b = int(b)
avg = ((a+b)/2)
print("avg of a and b is", avg)