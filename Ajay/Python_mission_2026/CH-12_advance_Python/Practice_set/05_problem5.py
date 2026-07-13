# store the multiplication table generated in problem 3 in a file name Table.txt

a = int(input("Enter Number: "))

table = [a*i for i in range(1,11)]

with open("Table.txt", "a") as f:
    f.write(str(table))
    