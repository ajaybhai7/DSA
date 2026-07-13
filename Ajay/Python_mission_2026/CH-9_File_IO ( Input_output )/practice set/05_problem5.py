''' repeate program 4 a list of such word censored'''

words = ["Donkey", "Donkeys", "is", "Good", "good", "a"]

# Read file

with open("file.txt", "r", encoding="utf-8")as f:
    # to open file in Such a Mode
    file = f.read()
    # to read file

for word in words:
    # A loop which will check the word = i in words 
    file = file.replace(word, "#" * len(word))

# Write file

with open("file.txt", "w", encoding="utf-8") as f:
    f.write(file)

print("Replaced successfull....")