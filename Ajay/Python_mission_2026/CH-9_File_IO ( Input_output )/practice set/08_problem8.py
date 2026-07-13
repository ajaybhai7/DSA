# Write a Program to make a copy of a txt file "This.txt" 

with open("this.txt", "r")as f:
    file = f.read()

with open("CopyThis.txt", "w")as f:
    f.write(file)

