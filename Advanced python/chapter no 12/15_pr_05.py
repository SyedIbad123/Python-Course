# Program to store a multiplication tables generated in problem 3 in a file.

num = int(input("Enter your number : "))
table = [num*i for i in range(1,11)]
print(table)
with open("tables.txt" , "a") as f:
    f.write(str(table))
    f.write("\n")