# Taking input from the user to print a multiplication table

def multi():
    n = int(input("Enter a number for a table: ")) # taking input from the user 

    for i in range(1, 11): # giving range 1 to 11 called argument as a if else 
        print(f"{n} x {i} = {n*i}") # printing final code one by one 

multi() # Calling function to run above the code