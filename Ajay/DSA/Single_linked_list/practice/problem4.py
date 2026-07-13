# doing problem 3 in another way 

def palindrome(): #Defining a function 
    word = input("Enter a Word to check palindrome or not: ") # Taking input from the user

    reverse_word = word[::-1] # reversing the word input

    if word == reverse_word: # Giving argumnet for tru or false
        print(f"Yes {word} is a palindrome!") # if true print this
    
    else: # if False 
        print(f"No {word} is not a palindrome!") # print this
    
palindrome() # Calling function to run the entire code 