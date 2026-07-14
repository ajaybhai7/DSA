# # write a program to print a maximum or minimum number of given list

# def max_min():
#     my_list = [15, 3, 89, 42, 1]
#     print(f"The maximum number is : {max(my_list)}")
#     print(f"The minimum number is : {min(my_list)}")

# max_min()


# In another way
def max_min(any_list): # Defining a function inside any list that we will give later

    sabse_bada = max(any_list) # Maximum value of anylist
    sabse_chota = min(any_list) # Minimum value of anylist

    return sabse_bada, sabse_chota # returning both variable

list1 = [12, 4, 6, 565, 7, 32, 42] # Defining a lis1
list2 = [23, 34, 64, 66, 232, 234, 23, 22] # Deining list2

bada, chota = max_min(list1) # Getting varial of return value the first return, and second return 
print(f"List1 -> Max: {bada}, Min: {chota}")

bada1, chota1 = max_min(list2)
print(f"List2 -> Max: {bada1}, Min: {chota1}") #printin Output 
