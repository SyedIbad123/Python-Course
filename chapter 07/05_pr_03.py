# Program to find whether the given number is prime or not...

num = int(input("Enter a number : "))
prime = True            # Here we can assign a value of prime variable

for i in range(2, num):
    if(num%i == 0):
        prime = False
        break
if prime:
    print("This is prime number")
else:
    print("This is not a prime number")