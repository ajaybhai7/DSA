# Can you change the self parameter inside a class to something else
# (Say "Ajay") try change to "slf" or "Ajay" and see the effect



from random import randint
class Train:

    # def __init__(self, trainNo):
    #     self.trainNo = trainNo
        
    def book(slf,trainNo, to):
        print(f"Ticket is booked in train no: {trainNo} from {fro} to {to}")

    def getStatus(slf):
        print(f"Trin no: {trainNo} is running on time")

    def getFare(slf,trainNo, to):
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
