# Program to calculate square,cube and sqrt using OOP..

class calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"The value of {self.num} square is {self.num**2}")

    def cube(self):
        print(f"The value of {self.num} cube is {self.num**3}")

    def sqrt(self):
        print(f"The value of {self.num} sqrt is {self.num**0.5}")


a = calculator(3)
a.square()
a.cube()
a.sqrt()
