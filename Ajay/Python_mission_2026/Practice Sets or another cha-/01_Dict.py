d = {}

name = input("Enter your name: ")
language = input("Enter your Language: ")
d.update({name: language})

name = input("Enter your name: ")
language = input("Enter your Language: ")
d.update({name: language})

name = input("Enter your name: ")
language = input("Enter your Language: ")
d.update({name: language})

name = input("Enter your name: ")
language = input("Enter your Language: ")
d.update({name: language})

print(d)

'''
Output:
Enter your name: Ajay
Enter your Language: Hindi
Enter your name: Vijay
Enter your Language: Englisj
Enter your name: Radha
Enter your Language: Bengali
Enter your name: Ram
Enter your Language: English 
{'Ajay': 'Hindi', 'Vijay': 'Englisj', 'Radha': 'Bengali', 'Ram': 'English '}
'''