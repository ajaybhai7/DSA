''' A file contains a word "Donkey" multiple times. You need to
write a program which replace this word with #### by updating
the same file'''


# File padho 
with open("file.txt", "r", encoding="utf-8") as f:
    file = f.read()

# File replace karo
file = file.replace("*****", "Donkey")

# File write karo

with open("file.txt", "w", encoding="utf-8") as f:
    f.write(file)

print("Sucessfully Changed.....")