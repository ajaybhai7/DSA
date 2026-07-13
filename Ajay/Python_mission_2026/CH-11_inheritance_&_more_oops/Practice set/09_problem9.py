# override the __len__() method on vector of problems 5 to 
# display the dimension of the vector 

class vector:
    def __init__(self, l):
        self.l = l

    def __len__(self):
        return len(self.l)

v = vector([1, 3, 4, 6, 2])

print(len(v))

