# Write a function to repete a word 

def repeat_word(word, repeat):


    for i in range(repeat):
        return word*repeat
    

word = input("Enter a Word: ")
repeat = input("How times to repeat: ")

dohrana = repeat_word(word, repeat)

print(dohrana)