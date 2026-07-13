# Write a class Train which has method to book
# a ticket, get status (no of seats) and get
# fare information of train running under 
# indian railway

from random import randint
class Train:

    # def __init__(self, trainNo):
    #     self.trainNo = trainNo
        
    def book(self,trainNo, to):
        print(f"Ticket is booked in train no: {trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Trin no: {trainNo} is running on time")

    def getFare(self,trainNo, to):
        print(f"Ticket fare in train no: {trainNo} from {fro} to {to} is : {randint(222,2131)}")

    @staticmethod
    def greet():
        print("==== Happy Journey ====")
ff = fro=input("Enter From : ")
tt = to=input("Enter TO: ")
trainNo = (1245455)

Train.book(trainNo, ff, tt)
Train.getStatus(trainNo)
Train.getFare(trainNo, ff, tt)
