# Program to print the multiplication table of given number by for and while loop...


# For loop...
num = int(input("Enter the number"))
for i in range(1,11):
    print(str(num) + " X " + str(i) + " = " + str(i*num)) # Here we use concatinating the srings so wo must first convert integer into string...
    
    
    
# While loop
num = int(input("enter the number : "))
i = 1
while i<=10:
    print(num, "X", i, "=", num * i)
    i = i+1