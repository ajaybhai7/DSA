# Write a function to repete a word 

def repeat_word(word, repeat):

    result = ""
    for i in range(repeat):
        result = result + word
    
    return result
    

word = input("Enter a Word: ")
repeat = int(input("How times to repeat: "))

dohrana = repeat_word(word, repeat)

print(dohrana)