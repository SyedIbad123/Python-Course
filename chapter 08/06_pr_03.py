# Program to find the sum of first n natural numbers using recursive function...

num = int(input("Enter a Number : "))
def sum_recursive(num):
    if num <= 1:
        print("Invalid number ! Please input a positive integral value")
    else:
        return num*(num+1)/2

n = sum_recursive(num)
print("The sum of first n natural number is : " , n)