# CLASS METHOD...
# 01 : The classmethod() is an inbuilt function in Python, which returns a class method for a given function.
# 02 : A class method takes cls as the first parameter.
# 03 : A class method can access or modify the class state
# 04 : Class methods must have class as a parameter.
# 05 : @classmethod decorator is used to create a class method.

class Employee:
    company = "Hyundai"
    salary = 1000
    location = "Islamabad"

    # def changeSalary(self,sal):     # Alternative and hard method
    #     self.__class__.salary = sal
    @classmethod
    def changeSalary(cls,sal):
        cls.salary = sal

e = Employee()
print(e.salary)
e.changeSalary(500)
print(e.salary)
