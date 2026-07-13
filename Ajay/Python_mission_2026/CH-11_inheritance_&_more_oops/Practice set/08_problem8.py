class vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self, other):
        result = vector(self.i + other.i, self.j + other.j, self.k + other.k)
        return result

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"


v1 = vector(1, 3, 5)
v2 = vector(3 , 6, 2)

print(v1 + v2)

