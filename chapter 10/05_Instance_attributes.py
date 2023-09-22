# INSTANCE ATTRIBUTES IN OOPs.
# 01 : Instance attributes are not shared by objects.
# 02 : Every object has its own copy of the instance attribute (In case of class attributes all object refer to single copy).
# 03 : Instance attribute taje preference over class attributes during assignment and retrievel.

# Example..
class Employee:
    company = "Microsoft"

Ibad = Employee()
Mahad = Employee()
Ibad.salary = 1000
Mahad.salary = 2000
print(Ibad.company)
print(Mahad.company)
print(Ibad.salary)
print(Mahad.salary)