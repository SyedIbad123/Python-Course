# RAISING EXCEPTIONS...
# 01 : We can exception using the raise keyword in python..


def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good")

a = input("Enter a number : ")
b = increment(a)
print(b)
    

