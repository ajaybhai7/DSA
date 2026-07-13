from random import randint

class Train:
    def book(self, fro, to):
        print(f"Ticket is booked in Train No. {trainNo} is From {fro} to {to}")

    def getStatus(self):
        print(f"The train no {trainNo} running on time")

    def getFare(self,fro, to):
        print(f"The train no {trainNo} from {fro} to {to} Total Fare is {randint(750, 2000)}")

trainNo = 135656
fro = input("Enter From: ")
to = input("Enter To: ")

Train.book(trainNo, fro, to)
Train.getStatus(trainNo)
Train.getFare(trainNo, fro, to)