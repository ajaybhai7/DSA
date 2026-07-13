def count_vowel(): # making a function

    a = input(str("Enter Any word to count vowel: ")) # taking input a word 

    a = a.lower() # for input workd in lower and upper case both

    vowel = "a, e, i, o, u" # defining vowel

    count = 0 # for adding count of vowel in my word 

    for word in a: # loop for printing word sequencily and store in word variable
        if word in vowel: # if word in vowel 
            count = count + 1 # add 1 in count 
            
    print("total Vowels = ", count) # print the final result 

count_vowel() # calling function