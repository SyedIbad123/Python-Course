# CLASS ATTRIBUTES IN OOPs..
# 01 : Class attributes belong to the class itself they will be shared by all the instances. Such attributes are defined in the class body parts usually at the top, for legibility.
# 02 : An attribute that belongs to the class rather than a particular object.


# Example..
class Employee:
    company = "Microsoft"

Ibad = Employee()
Mahad = Employee()
print(Ibad.company)
print(Mahad.company)

Employee.company = "Amazon"
print(Ibad.company)
print(Mahad.company)