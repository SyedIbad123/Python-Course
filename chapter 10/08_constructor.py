# CONSTRUCTOR IN OOPs..
# 01 : Constructors are generally used for instantiating an object.
# 02 : The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created.
# 03 : Types of constructors : 
# default constructor: The default constructor is a simple constructor which doesn’t accept any arguments. Its definition has only one argument which is a reference to the instance being constructed.
# parameterized constructor: constructor with parameters is known as parameterized constructor. The parameterized constructor takes its first argument as a reference to the instance being constructed known as self and the rest of the arguments are provided by the programmer.
# 04 : In Python the __init__() method is called the constructor and is always first run when an object is created. It takes self argument and take further argument..
'''Syntax of constructor declaration : 

         def __init__(self):
             # body of the construc         '''


# ExAmPlE.


class employee():
    def __init__(self,name,salary,job):
        self.name = name
        self.salary = salary
        self.job = job
        print("employee is created")
        
    def details(self):
        print(f"The name of employee is {self.name}")
        print(f"The salary of employee is {self.salary}")
        print(f"The job of employee is {self.job}")
        
ibad = employee("ibad",1000,"developer")
# ibad = employee() ==> This throws a positional arument error..
ibad.details()


