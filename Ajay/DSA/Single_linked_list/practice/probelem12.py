# Write a function to repete a word 

def repeat_word(word, repete):

    word = word
    repete = repete

    return word*repeat
    

word = input("Enter a Word: ")
repeat = input("How times to repeat: ")

dohrana = repeat_word(word, repeat)

print(dohrana)