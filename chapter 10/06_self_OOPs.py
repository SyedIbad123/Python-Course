# SELF PARAMETER IN OOPs...

# 01 : Self represents the instance of the class. By using the “self”  we can access the attributes and methods of the class in python. It binds the attributes with the given arguments.
# 02 : The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.


# Example..
class Employee:
    company = "Microsoft"
    def Getsalary(self, greet):
        print(f'Salary for this employee working in {self.company} is {self.salary}\n{greet}')
    
Ibad = Employee()
Ibad.salary = 100000
Ibad.Getsalary("THANKS !")
