

usr_input = input("aaj ki diary mein kya likhna hai?: ")
with open("my_diary.txt", 'w') as f:
    f.write(usr_input)

with open ("my_diary.txt", 'r') as a:
    infile = a.read()

print(infile)