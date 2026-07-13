""" Write a program to read a text from a given file 'poem.txt' and 
find out whether it containes the word 'twinkle' """

file = open("poem.txt")
contant = file.read()
if "twinkle" in contant:
    print("The word 'Twinkle' is present in this file")
    
else:
    print("Twinkle not present in this file ")

file.close()
