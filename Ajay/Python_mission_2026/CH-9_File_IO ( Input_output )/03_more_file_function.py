# This function for single line reading, this reads
# line squenceially

file = open("Write.txt")
read1 = file.readline() #Read line -> 1 
read2 = file.readline() #Read line -> 2
print(read1, end="") # Print Read line ->1 Jo usne read kiya hai
print(read2) # Print Read line ->2 Jo usne read kiya hai
file.close()


'''If we want read all lines in the text file then we use
readlines function to read all line entire the text  file. Ex- '''

f = open("Write.txt")

read = f.readlines()
print(read)
f.close()

''' it's gives output like this form
['My name is Ajay Kumar\n', 'What about you?\n']
it gives in a list form all entire text
\n = it shows the next line begin from there.
'''
