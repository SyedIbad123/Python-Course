# Program to create a class soring info about programmers..

class programmer:
    comapany = "Microsoft"
    def __init__(self,name,salary,product):
        self.name = name
        self.salary = salary
        self.product = product
    def details(self):
        print(f'The name of the {self.comapany} programmer is {self.name}.The salary is {self.salary} and the product is {self.product}')
ibad = programmer("ibad",10000,"MS-office")
shahzaib = programmer("shahzaib",80000,"github")
ibad.details()
shahzaib.details()

        

