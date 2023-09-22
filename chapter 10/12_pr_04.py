# Program to create a class train to get status of booking tickets..

from unicodedata import name


class train:
    def __init__(self,name,totalseats,seats,fare,category):
        self.name = name
        self.seats = seats
        self.fare = fare
        self.category = category
        self.totalseats = totalseats
        
    def getstatus(self):
        print(f"The name of the train is : {self.name}")
        print(f"The quantity of Total seats available in this train is : {self.totalseats}")
        print(f"The Remaining seats available in this train is : {self.seats}")
    
    def getInfo(self):
        print(f'The category is {self.category}')
        print(f"The fair of the train is : Rs.{self.fare}")
        
    def bookTicket(self):
        if(self.seats>0):
            print(f"Congratulations ! Your ticket has been booked. Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print(f"Sorry ! Seats are full")
        
karakoram = train("Karakoram Express : 23890 (Train number)", 1000, 550, "1800 (economy class)", "Economy class")
karakoram.getstatus()
karakoram.bookTicket()
karakoram.getstatus()
karakoram.getInfo()