'''
Write a program to generate multiplication table from 2 to 20
and write it to the new different file in a folder for a 
13 years old.. '''
def generatetable(n):
    table = ""    
    for i in range(1, 11):
        table += f"{n} x {i} = {n*i}\n"
        # for looping 1, to 10 
    
    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)


for i in range(2, 21):
    generatetable(i)


# It will generate a folder that name be tables in the tables 
# folder it will generate a multiplication table in it,
# in different - 2 txt file 

