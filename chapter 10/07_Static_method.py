# STATIC METHOD IN OOPs...
# 01 : Sometimes we need a function that doesn't use the self parameter. We can define a static method.
# 02 : A static method is a method which is bound to the class and not the object of the class.
# 03 : It is present in a class because it makes sense for the method to be present in class. A static method does not receive an implicit first argument.


# Example..
class Employee:
    company = "Microsoft"
    def Getsalary(self, greet):
        print(f'Salary for this employee working in {self.company} is {self.salary}\n{greet}')
    
    @staticmethod
    def greet():      # Here we canot write self bcz of static method...
        print("Good Morning, Sir" )
    
Ibad = Employee()
Ibad.salary = 100000
Ibad.Getsalary("THANKS !")
Ibad.greet()
