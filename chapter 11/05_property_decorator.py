# PROPERTY DECORATOR..
# 01 : It is a built-in decorator in Python which is helpful in defining the properties effortlessly without manually calling the inbuilt function property().
# 02 : 

class employee:
    comapny = "Honda"
    salary = 1300
    salaryBonus = 800
    
    
    @property
    def totalSalary(self):
        return self.salary + self.salaryBonus
    
    @totalSalary.setter
    def totalSalary(self,val):
         self.salary = val - self.salaryBonus


e = employee()
print(e.totalSalary)
e.totalSalary = 1500
print(e.salary)
print(e.salaryBonus)