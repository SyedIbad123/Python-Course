# Program to print a multiplication in reversed order..


num = int(input("Enter the number"))
for i in reversed(range(1,11)):    # Python reversed() method returns an iterator that accesses the given sequence in the reverse order.
    print(str(num) + " X " + str(i) + " = " + str(i*num))