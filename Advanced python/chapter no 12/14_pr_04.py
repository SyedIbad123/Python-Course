# Program to display a/b where a and b are integers. If b = 0, display infinite by handling the zerodivisionzero.

a = int(input("enter a number :"))
b = int(input("enter a number :"))

try:
    print(a/b)
except:
    if a==0:
        print("Undefined")
    else:
        print("Infinite")