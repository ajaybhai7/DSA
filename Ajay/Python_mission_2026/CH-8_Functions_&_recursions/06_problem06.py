# Write a function to remove a given word in a list and strip it at the same time

def rem(l, word):
    n = []
    for item in l :
        if not (item == word):
            n.append(item.strip(word))
    return n
a = input("Enter word to remove : ")
l = [1, 4, 2, 5, "Ajay", "Arun"]
print(l, a)