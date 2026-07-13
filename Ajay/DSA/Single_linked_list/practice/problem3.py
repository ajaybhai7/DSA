# Write a program to print palindrome or not taking word from the user as a input

def palindrome():
    x = input("Enter a word to check palindrome or not: ")
    for word in x:
        if word.startswith == word.endswith:
            print(f"Yes {x} is a palindrome!")
            break

        else:
            print(f"no {x} is not a palindrome!")
            break

palindrome()