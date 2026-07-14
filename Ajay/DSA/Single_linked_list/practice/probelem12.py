# Write a function to repete a word 

def repeat_word(word, repete):

    final = str(word)*repete
    return final

word = input("Enter a Word: ")
repeat = input("How times to repeat: ")

dohrana = repeat_word(word, repeat)

print(dohrana)