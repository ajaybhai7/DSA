text = "\nMy name is Ajay Kumar"

file = open("file.txt", "a") # For open file in append mode (a)

file.write(text) 
"""
The `write` function is essential for writing data 
and overwriting existing content in a program."""

file.close() #After completion closing door.  

#I ran it four times, and it added this four times.
"""
This is a good boy

My name is Ajay Kumar
My name is Ajay Kumar
My name is Ajay Kumar
My name is Ajay Kumar
My name is Ajay Kumar

"""