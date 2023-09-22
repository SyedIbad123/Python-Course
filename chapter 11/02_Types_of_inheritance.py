# TYPES OF INHERITANCE.
''' There are 3 types of inheritance.
     01 : Single ineritance
     02 : Multiple inheritance
     03 : Multilevel inheritance'''

# A - Single inheritance.
# 01 : When a child class inherits from only one parent class, it is called single inheritance.

# Example : 
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




# B - Multiple inheritance.
# 01 : When a child class inherits from multiple(more than one) parent classes, it is called multiple inheritances. 

class employee:
     company = "visa"
     eCode= 0

class freelancer:
     company = "fiverr"
     level = 0

     def upgradeLevel(self):
          self.level = self.level + 1

class programmer(employee , freelancer): # The priority of first argument is greater.
     name = "Ibad"

p = programmer()
p.upgradeLevel()
print(p.company)
print(p.name)



# C - Multilevel inheritance.
# 01 : When we have a child and grandchild relationship. 
# 02 : when a child class becomes a parent for another child class.


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
          
p = person()
p.takeBreath()
e = employee()
pr = programmer()