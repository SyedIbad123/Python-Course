# SUPER CLASS IN OOP..
# 01 : The Python super() function returns objects represented in the parent’s class and is very useful in  multiple and multilevel inheritances to find which class the child class is extending first.
# 02 : It is used to access the methods of a super class in the derived class.

class person:
    country = "Pakistan"

    def takeBreath(self):
          print("I am breathing...")
          
class employee(person):
    company = "Toyota"

    def getSalary(self):
        print(f"The salary is {self.getSalary}")
          
    def takeBreath(self):
        print("I am an employee , I am breathing")

class programmer(employee):
    company = "Fiverr"

    def getSalary(self):
        print(f"No salary to programmers")
          
    def takeBreath(self):
        super().takeBreath()                 # Here super function prints super class
        print("I am a programmer , I am breathing++..")
          
p = person()
p.takeBreath()
e = employee()
e.takeBreath()
pr = programmer()
pr.takeBreath()