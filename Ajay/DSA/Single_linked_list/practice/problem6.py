# write a program to print even number from exiting list to append in new list

def list_g(): # Deifining a function
    
    # Taking Input from the user will how long the list
    n = int(input("Enter number to how much numbers in your list: "))

    # Creating a empty to add number in it using aappend method 
    old_list = [] 

    # starting a loop by giving an input from the user
    for i in range(1, n):

        #taking input to add number in the old_list
        a = int(input(f"Enter {i} number: "))

        #appending numbers in the list using append method sequencialy
        old_list.append(a)

        #Defining a new_list
    new_list = []

    #starting loop of old list to check where is even number
    for x in old_list:

        # if number x is even append it into the new_list
        if x % 2 == 0:

            # appending number who's are even in the old list
            new_list.append(x)

    # printing the final even numbers list our new_list
    print(f"New Even Number List is : {new_list}")

list_g() # Calling the function to excute above the code
