# INERITANCE IN OOPs..
# 01 : Inheritance allows us to define a class that inherits all the methods and properties from another class(parent).
# 02 : Inheritance is the way of creating a new class from an existing class.
'''The syntax for creating child class is : 
        class name:
           code
        class name2(name) # We pass a parent class here for parameter.
           code'''
# 03 : We can overwrite or add new attributes and methods in child class.


class employee:
    comapny = "Google"

    def showdata(self):
        print("This is an employee")
    
class programmer(employee):
    language = "python"

    def getLanguage(self):
        print(f"The language is {self.language}")
        
    def showdata(self):
        print("This is an programmer")
    
e = employee()
e.showdata()
p = programmer()
p.showdata()
