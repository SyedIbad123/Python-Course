# Program to allow your 3 friends to enter their fav language as values and use keys as their names. Assume that the names are unique..

favlang = {}

a = input("Enter your fav language saad\n")
b = input("Enter your fav language shahzaib\n")
c = input("Enter your fav language zaid\n")

favlang["saad"] = a
favlang["shahzaib"] = b
favlang["zaid"] = c
print(favlang)

# keys should be unique in dictionary
# values should not unique (chlega...)